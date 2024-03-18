from models.__init__ import CURSOR, CONN
from models.campaign._Campaign import CampaignMethods
from models.dungeon_master.Dungeon_Master import DungeonMaster

class Campaign(CampaignMethods):

    all = {}

    def __init__(self, name, dungeon_master_id, id=None):
        self.id = id
        self.name = name
        self.dungeon_master_id = dungeon_master_id

    # def __repr__(self):
    #     return f"({self.id}) Campaign: {self.name}, Dungeon Master: {DungeonMaster.find_by_id(self.dungeon_master_id).name}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Campaign name must be a non-empty string."
            )
    
    @property
    def dungeon_master(self):
        return self._dungeon_master_id
    
    @dungeon_master.setter
    def dungeon_master(self, id):
        if type(id) is int and DungeonMaster.find_by_id(id):
            self._dungeon_master_id = id
        else:
            raise ValueError(
                "Dungeon Master ID must reference a Dungeon Master in the Database."
            )
        