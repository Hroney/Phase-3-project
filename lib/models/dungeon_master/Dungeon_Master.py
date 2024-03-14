from models.__init__ import CURSOR, CONN
from models.dungeon_master._Dungeon_Master import DungeonMasterMethods

class DungeonMaster(DungeonMasterMethods):

    all = {}

    def __init__(self, name, modality, id = None):
        self.name = name
        self.modality = modality
        self.id = id

    # def __repr__(self):
    #     return f"({self.id}) Name: {self.name}, Sessions are held: {self.modality}"

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
    def modality(self):
        return self._modality
    
    @modality.setter
    def modality(self, modality):
        if isinstance(modality, str) and len(modality):
            self._modality = modality
        else:
            raise ValueError(
                "Modality must be a non-empty string."
            )
    