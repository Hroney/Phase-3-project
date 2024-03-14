#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.campaign.Campaign import Campaign
from models.dungeon_master.Dungeon_Master import DungeonMaster
import ipdb

def reset_database():
    Campaign.drop_table()
    DungeonMaster.drop_table()

    Campaign.create_table()
    DungeonMaster.create_table()


    sarah = DungeonMaster.create("Sarah", "In-person")
    baron = DungeonMaster.create("Baron", "Online")
    smith = DungeonMaster.create("Smith", "Online")
    john = DungeonMaster.create("John", "In-person")
    shadow_land = Campaign.create("Shadow Land", baron.id)
    palace_of_the_dead = Campaign.create("Palace of the Dead", sarah.id)
    space_place = Campaign.create("Space Place", john.id)
    rat_kingdom = Campaign.create("Rat Kingdom", baron.id)
    wheel_of_fun = Campaign.create("Wheel of Fun", smith.id)


    ipdb.set_trace()


reset_database()
