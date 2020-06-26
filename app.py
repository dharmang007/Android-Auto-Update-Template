from flask import Flask, request
import json
from tinydb import TinyDB,Query
from updatemanager import Application1, updatemanager_app, UpdateManager

app = Flask(__name__)
app.register_blueprint(updatemanager_app)
db = TinyDB('db.json')
@app.route('/', methods=['GET'])
def get_data():
    return json.dumps({"items": db.all()})

@app.route('/latest-version',methods=['GET'])
def get_latest_version():
    """
    Gets latest version for the given app
    """
    try:
        print(request.args.get('appName'))
        application = Application1()
        
        versions_list = application.getVersion(str(request.args.get('appName')))
        latest = '0.0'
        for doc in versions_list:
            if doc['version'] > latest:
                latest = doc['version']
        return json.dumps({"latest_version":latest})
    except Exception as e:
        print("Error "+ str(e))

@app.route('/versions', methods=['GET'])
def get_app_versions():
    """
    This method gets list of all the version for a specific app
    For simplicity, I have just used Application1 
    """
    try:
        print(request.args.get('appName'))
        application = Application1()
        appName = request.args.get('appName')
        versions = application.getVersion(appName)
        return json.dumps({"latest_version": versions})
    except Exception as e:
        print(str(e))

    


@app.route('/send-update', methods=['GET','POST'])
def update():
    application = Application1()
    latest_v = application.send_update("4.0")  
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
