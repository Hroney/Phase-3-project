from models.__init__ import CURSOR, CONN
from models.player._Player import PlayerMethods
from models.campaign.Campaign import Campaign
import re

class Player(PlayerMethods):
    
    all = {}

    def __init__(self, name, email, id = None):
        self.name = name
        self.email = email
        self.id = id

    def __repr__(self):
        return f"({self.id}) Name: {self.name}, Email: {self.email}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string."
            )
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  
        if re.fullmatch(regex, email):
            self._email = email
        else:
            raise ValueError(
                "Name must be a proper email address."
            )