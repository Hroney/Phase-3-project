from models.__init__ import CURSOR, CONN
from models.campaign._Campaign import CampaignMethods
from models.dungeon_master.Dungeon_Master import DungeonMaster

class Campaign(CampaignMethods):

    all = {}

    def __init__(self, campaign_name, dungeon_master_id, id=None):
        self.id = id
        self.campaign_name = campaign_name
        self.dungeon_master_id = dungeon_master_id

    def __repr__(self):
        return f"({self.id}) Campaign: {self.campaign_name}, Dungeon Master: {DungeonMaster.find_by_id(self.dungeon_master_id).name}"

    @property
    def campaign_name(self):
        return self._campaign_name
    
    @campaign_name.setter
    def campaign_name(self, name):
        if isinstance(name, str) and len(name):
            self._campaign_name = name
        else:
            raise ValueError(
                "Campaign name must be a non-empty string."
            )
    
    @property
    def dungeon_master(self):
        return self._dungeon_master_id
    
    @dungeon_master.setter
    def dungeon_master(self, dm_id):
        if type(dm_id) is int and DungeonMaster.find_by_id(dm_id):
            self._dungeon_master_id = dm_id
        else:
            raise ValueError(
                "Dungeon Master ID must reference a Dungeon Master in the Database."
            )
        