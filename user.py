import abc
from tinydb import TinyDB,Query
import json
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

    def send_update_notification(self,new_version):
        
        """
        send the API response to send the update to client device
        """
        
        pass 
        


    
        