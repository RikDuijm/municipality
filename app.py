import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId # Convert in Bson-bject to retrieve record in MongoDB by report ID
from bson import Binary
import re
import bcrypt #https://pypi.org/project/bcrypt/
# Libraries necesary to store smaller binary files in
import uuid
from bson.binary import Binary, UUIDLegacy, STANDARD
from bson.codec_options import CodecOptions

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'municipality'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

# Create an instance of PyMongo. Add the app into that with a constructor method.
mongo = PyMongo(app)

"""
- Make connection to the database
- render a template (reports.html)
- supply the reports collection (reports=mongo.db.reports,), which will be returned from making a call directly to Mongo.
- with the find() method, which will return everything.
"""

# Because of the / decorator the default function that will be called will be get_reports. Change this later on!
@app.route('/')
def index():
    return render_template("index.html")

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

# https://pypi.org/project/bcrypt/
# https://stackoverflow.com/questions/38246412/bytes-object-has-no-attribute-encode
# https://www.youtube.com/watch?v=vVx1737auSE
# '''
# >>> import bcrypt
# >>> password = b"super secret password"
# >>> # Hash a password for the first time, with a randomly-generated salt
# >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# >>> # Check that an unhashed password matches one that has previously been
# >>> # hashed
# >>> if bcrypt.checkpw(password, hashed):
# ...     print("It Matches!")
# ... else:
# ...     print("It Does not Match :(")
# '''

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), salt)

            users.insert_one({'username': request.form['username'], 'password' : hashed})
            session['username'] = request.form['username']
            return render_template('login.html')

        else:
            return render_template('existinguser.html')
    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username' : request.form['username']})
        if login_user:
            salt = request.form['password'].encode('utf-8')
            input_password = bcrypt.hashpw(salt, login_user['password'])
            if input_password == login_user['password']:
                session['username'] = request.form['username']
                session['logged_in'] = True
                if session['username'] == 'admin':
                    return redirect("get_reports")
                else:
                    return render_template('addreport.html')
            else:
                return render_template('loginerror.html')
        else:
                return render_template('loginerror.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return render_template('index.html')

@app.route('/get_reports')
def get_reports():
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
    reports.remove({'_id' : ObjectId(report_id)})
    return redirect(url_for('get_reports'))

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/street/<streetname>')
def street(streetname):
    problems_in_street = mongo.db.reports.find_one_or_404({'streetname' : streetname})
    return f'''
           <h1>{streetname}</h1>
           <img src="{url_for('file', filename = streetname['image-name'])}" width ="300">
           '''


if __name__ == '__main__':
    app.secret_key = 'geheimpje'
    app.run(host="0.0.0.0", port=5000, debug=True)
