import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import Binary
import re

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

        return render_template("reports.html", reports=mongo.db.reports.find())


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
    app.run(debug=True)
