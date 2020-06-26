import abc
from tinydb import TinyDB,Query
import json
from flask import Blueprint

updatemanager_app = Blueprint('updatemanager_app',__name__)
db = TinyDB('db.json')
class UpdateManager(abc.ABC):
    """
    Interface for managing updates of multiple apps
    """
    def __init__(self):
        pass

    @abc.abstractmethod
    def subscribe(self, user):
        pass

    @abc.abstractmethod
    def unsubscribe(self, user):
        pass 
    
    @abc.abstractmethod
    def send_update(self,new_version):
        pass

    def getVersion(self,app_name):
        q = Query()
        versions = db.search(q.app_name == app_name)
        print(versions)
        return versions

class Application1(UpdateManager):
    """
    Concreate Class which manages updates of Application1
    """
    def __init__(self,supported_os=[],previous_versions=[],users=[],latest_supported_version=""):
        self._supported_os = supported_os
        self._previous_versions = previous_versions
        self._users = users
        self._latest_supported_version = latest_supported_version

    def subscribe(self, user):
        print("User installed this app!")
        # TODO: add into Database
        # This will be called when the app is installed by the user
        self._users.append(user)
        return 

    def unsubscribe(self, user):
        print("User uninstalled this app!")
        # TODO: remove from Database
        # This can be used when the user uninstalls the app 
        # OR a special code snippet can be added which will manage if the user has disabled the update notification  
        self._users.remove(user) 
        return 

    
    def send_update(self,new_version):
        # TODO: Add the code to add new version for Application1 in DB
        # send notification from server to users to update the app from notifications
        self._previous_versions.append(self._latest_supported_version)
        self._latest_supported_version = new_version
        db = TinyDB('db.json')
        db.insert({'app_name':'Application1', 'version':new_version,'location':'','os':'os_1'})
        for user in self._users:
            user.get_update_notification(new_version)
        
        return json.dumps(db.all())

"""
Users are the different devices which will recieve the updates
UserInterface is implemented by cconcrete  User class 
"""
class UserInterface(abc.ABC):

    @abc.abstractclassmethod
    def send_update_notification(self,new_version):
        pass

class Users:
    def __init__(self,name,email,address):
        self._name = name
        self._email = email
        self._address = address

    def edit_user(self, user):
        """
        This method can be used to update user 
        """
        pass

    def get_user(self,email):
        
        """
        To retrieve the user details 
        """
        pass

    @updatemanager_app.route('/get-notification', methods=['GET', 'POST'])
    def get_update_notification(self,new_version):
        
        """
        send the API response to send the update to client device
        """
        

