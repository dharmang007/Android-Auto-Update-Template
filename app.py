from flask import Flask, request
import json
from tinydb import TinyDB,Query
from updatemanager import Application1


app = Flask(__name__)
db = TinyDB('db.json')
@app.route('/', methods=['GET'])
def get_data():
    return json.dumps({"items": db.all()})

@app.route('/versions', methods=['GET'])
def get_app_versions(appName):
    print(request.args.get('appName'))
    application = Application1()
    appName = request.args.get('appName')
    versions = application.getVersion(appName)
    return json.dumps({"items": versions})


@app.route('/send-update', methods=['GET','POST'])
def update():
    application = Application1()
    latest_v = application.send_update("2.0")  
    return json.dumps({"latest_version":latest_v})

@app.route('/add-version', methods=['GET', 'POST'])
def add_version():
    """
    add-version endpoint will be used to add a new version of app into the db.json
    """
    print("Adding new version")

    return json.dumps(db.all())


    
    
if __name__ == '__main__':
    app.run()
