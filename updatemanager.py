import abc
from tinydb import TinyDB,Query
import json
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
    def __init__(self,supported_os=[],previous_versions=[],users=[],latest_support_version=""):
        self._supported_os = supported_os
        self._previous_versions = previous_versions
        self._users = users
        self._latest_support_version = latest_support_version

    def subscribe(self, user):
        print("User installed this app!")
        # TODO: add into Database
        self._users.append(user)
        return

    def unsubscribe(self, user):
        print("User uninstalled this app!")
        # TODO: remove from Database
        self._users.remove(user) 
        return 

    def send_update(self,new_version):
        # TODO: Add the code to add new version for Application1 in DB
        # send notification from server to users to update the app from notifications
        self._previous_versions.append(self._latest_support_version)
        self._latest_supported_version = new_version
        db = TinyDB('db.json')
        db.insert({'app_name':'Application1', 'version':new_version,'location':'','os':'os_1'})
        for user in self._users:
            user.send_update_notification(new_version)
        return json.dumps(db.all())

    


            

