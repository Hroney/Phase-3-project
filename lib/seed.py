from models.__init__ import CURSOR, CONN
from models.campaign.Campaign import Campaign
from models.dungeon_master.Dungeon_Master import DungeonMaster
# from models.player.Player import Player
# from models.player_campaign.Player_Campaign import PlayerCampaign

def seed_database():
    Campaign.drop_table()
    DungeonMaster.drop_table()
    # Player.drop_table()
    # PlayerCampaign.drop_table()
    Campaign.create_table()
    DungeonMaster.create_table()
    # Player.create_table()
    # PlayerCampaign.create_table()

    sarah = DungeonMaster.create("Sarah", "In-person")
    baron = DungeonMaster.create("Baron", "Online")
    smith = DungeonMaster.create("Smith", "Online")
    john = DungeonMaster.create("John", "In-person")

    shadow_land = Campaign.create("Shadow Land", baron.id)
    palace_of_the_dead = Campaign.create("Palace of the Dead", sarah.id)
    space_place = Campaign.create("Space Place", john.id)
    rat_kingdom = Campaign.create("Rat Kingdom", baron.id)
    wheel_of_fun = Campaign.create("Wheel of Fun", smith.id)

    # johnny = Player.create("Johnny", "coolGuy124@hotmail.com")
    # grant = Player.create("Grant", "coding_is_fun@gmail.com")
    # pablo = Player.create("Pablo", "senul_axulo26@hotmail.com")
    # perry = Player.create("Perry", "sutaci_roxa17@hotmail.com")
    # tim = Player.create("Tim", "hutchison_mckenna5@yahoo.com")
    # debbie = Player.create("Debbie", "gold_jovanny36@mail.com")
    # karol = Player.create("Karol", "hurstvickey99@yahoo.com")
    # meg = Player.create("Meg", "jeroldliu71@gmail.com")

    # PlayerCampaign.create(1,1)
    # PlayerCampaign.create(1,2)
    # PlayerCampaign.create(2,1)
    # PlayerCampaign.create(3,1)



seed_database()
print("Seeded database")
