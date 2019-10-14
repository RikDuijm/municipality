import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    })
    return render_template('search.html', query=orig_query, results=results)


# https://pypi.org/project/bcrypt/
# https://stackoverflow.com/questions/38246412/bytes-object-has-no-attribute-encode
# https://www.youtube.com/watch?v=vVx1737auSE
'''
>>> import bcrypt
>>> password = b"super secret password"
>>> # Hash a password for the first time, with a randomly-generated salt
>>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
>>> # Check that an unhashed password matches one that has previously been
>>> # hashed
>>> if bcrypt.checkpw(password, hashed):
...     print("It Matches!")
... else:
...     print("It Does not Match :(")
'''

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())

            users.insert({'name': request.form['username'], 'password' : hashed})
            session['username'] = request.form['username']
            return render_template('search.html')

        return 'That username already exists.'
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        if login_user:
            if bcrypt.checkpw(request.form['password'].encode('utf-8'), hashed):
                session['username'] = request.form['username']
                return redirect(url_for('get_reports'))
            else:
                return 'Invalid username/password combination.'
    return render_template('login.html')

@app.route('/get_reports')
def get_reports():
    return render_template("reports.html", reports=mongo.db.reports.find())

@app.route('/add_report')
def add_report():
    return render_template("addreport.html")

@app.route('/insert_report', methods=['POST'])
def insert_report():
    if 'image' in request.files:
        image = request.files['image']
        mongo.save_file(image.filename, image)
        mongo.db.reports.insert({'streetname' : request.form.get('streetname'), 'date' : request.form.get('date'), 'problem' : request.form.get('problem'), 'image' : image.filename})

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
    app.run(debug=True)
