import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo # Needed to connect Flask to the MongoDB
from bson.objectid import ObjectId # Convert in Bson-bject to retrieve record in MongoDB by report ID
from bson import Binary # Needed to upload and retrieve files.
import re # Needed for search functionality
import bcrypt #https://pypi.org/project/bcrypt/

app = Flask(__name__)

# Point Heroku to the config variable (MONGO_URI) to keep the production database connection string secret.
app.config["MONGO_DBNAME"] = 'municipality'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

# Create an instance of PyMongo. Add the app into that with a constructor method.
mongo = PyMongo(app)

"""
- Make connection to the database
- render a template
"""
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# Code used from https://github.com/5pence/recipeGlut and changed for my own needs
@app.route('/search')
def search():
    """Provides logic for search bar"""
    orig_query = request.args['query']
    # using regular expression setting option for any case
    query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
    # find instances of the entered word in streetname
    results = mongo.db.reports.find({
        '$or': [
            {'streetname': query},
        ]
    }).sort('date', -1)
    return render_template('search.html', query=orig_query, results=results)

@app.route('/register', methods=['POST', 'GET'])
def register():
    """Provides logic for search bar"""
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})
         # check if username already exists.
        if existing_user is None:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), salt)
            # safe username and password in MongoDB and log in immediately
            users.insert_one({'username': request.form['username'], 'password' : hashed})
            session['username'] = request.form['username']
            return redirect("add_report")
        else:
            return redirect("existinguser")
    return render_template('register.html')

@app.route('/existinguser')
def existing():
    return render_template("existinguser.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username' : request.form['username']})
        if login_user:
            salt = request.form['password'].encode('utf-8')
            input_password = bcrypt.hashpw(salt, login_user['password'])
            # check credentials and see if user is citizen or admin
            if input_password == login_user['password']:
                session['username'] = request.form['username']
                session['logged_in'] = True
                if session['username'] == 'admin':
                    return redirect("get_reports")
                else:
                    return redirect("add_report")
            # in case credentials are wrong
            else:
                return redirect("login_error")
        else:
                return redirect("login_error")
    return render_template('login.html')

@app.route('/login_error')
def login_error():
    return render_template('loginerror.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect("index")

@app.route('/get_reports')
def get_reports():
    # supply the reports collection (reports=mongo.db.reports,), which will be returned from making a call directly to Mongo.
    # with the find() method, which will return everything.
    return render_template("reports.html", reports=mongo.db.reports.find().sort('date', -1))

@app.route('/add_report')
def add_report():
    return render_template("addreport.html")

@app.route('/insert_report', methods=['POST'])
def insert_report():
    reports = mongo.db.reports
    reports.insert_one(request.form.to_dict())
    return redirect("get_reports")

@app.route('/edit_report/<report_id>')
def edit_report(report_id):
    # connecting with the correct report in the database
    the_report =  mongo.db.reports.find_one({"_id": ObjectId(report_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editreport.html', report=the_report,
                           categories=all_categories)

@app.route('/update_report/<report_id>', methods=['POST'])
def update_report(report_id):
    reports = mongo.db.reports
    reports.update({'_id' : ObjectId(report_id)},
      {
        'streetname':request.form.get('streetname'),
        'problem': request.form.get('problem'),
        'date': request.form.get('date'),
        'username' :  request.form.get('username'),
        'image': request.form.get('image'),
        'add_comment': request.form.get('add_comment'),
    })
    return redirect(url_for('get_reports'))

@app.route('/delete_report/<report_id>')
def delete_report(report_id):
    reports = mongo.db.reports
    # connecting with the correct report in the database
    reports.remove({'_id' : ObjectId(report_id)})
    return redirect(url_for('get_reports'))

if __name__ == '__main__':
    app.secret_key = os.getenv('SECRET_KEY')
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
