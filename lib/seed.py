from models.__init__ import CURSOR, CONN
from models.campaign.Campaign import Campaign
from models.dungeon_master.Dungeon_Master import DungeonMaster

def seed_database():
    Campaign.drop_table()
    DungeonMaster.drop_table()
    Campaign.create_table()
    DungeonMaster.create_table()

    sarah = DungeonMaster.create("Sarah Johnson", "In-person")
    baron = DungeonMaster.create("Baron Smith", "Online")

    shadow_land = Campaign.create("Shadow Land", baron.id)
    palace_of_the_dead = Campaign.create("Palace of the Dead", sarah.id)

seed_database()
print("Seeded database")
