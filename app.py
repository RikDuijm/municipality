import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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
@app.route('/get_reports')
def get_reports():
    return render_template("reports.html", reports=mongo.db.reports.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)