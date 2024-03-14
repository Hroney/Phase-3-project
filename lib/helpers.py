# lib/helpers.py
from models.campaign.Campaign import Campaign
from models.dungeon_master.Dungeon_Master import DungeonMaster
# from models.player.Player import Player
# from models.player_campaign.Player_Campaign import PlayerCampaign
import os



### Campaign Helpers ###

def list_campaigns():
    campaigns = Campaign.get_all()
    print("\nCampaign List:\n")
    for campaign in campaigns:
        print(f"{campaigns.index(campaign)+1}. {campaign.campaign_name}")
    return campaigns

def delete_campaign(campaign):
        clear_console()
        if campaign_ := Campaign.find_by_id(campaign.id):
            print(f'Campaign {campaign_.campaign_name} deleted.')
            campaign_.delete()
        else:
            clear_console()
            print(f"Campaign not deleted")

def update_campaign_name(campaign_):
    clear_console()
    print("\nEnter Campaign's new name")
    campaign_.campaign_name = input("> ")
    campaign_.update()
    clear_console()
    print(f"\nCampaign Updated: {campaign_.print_info()}")

def update_campaign_dm(campaign_):
    clear_console()
    print("\nEnter New Dungeon Master")
    dungeon_masters = list_dungeonmasters()
    try:
        input_value = int(input("> "))
        if input_value >0:
            campaign_.dungeon_master_id = dungeon_masters[input_value - 1].id
            campaign_.update()
            clear_console()
            print("\nCampaign Updated: ", campaign_.print_info())
        else:
            clear_console()
            print("Not a valid Dungeon Master")
    except IndexError or ValueError:
        clear_console()
        print("Not a valid Dungeon Master")


def create_a_campaign(dungeon_master_):
    clear_console()
    print("\nWhat's the Name of the new campaign?")
    try:
        campaign_ = Campaign.create(input("> "), dungeon_master_.id)
        clear_console()
        print(f"\n{campaign_.campaign_name} has been created! Good luck!")
    except Exception as exc:
        clear_console()
        print("Error creating Campaign: ", exc, "\n")

def cancel_a_campaign(dungeon_master_):
    clear_console()
    dms_campaigns = dungeon_master_.campaigns()
    if len(dms_campaigns):
        print("\n\n\n\n")
        for campaign in dms_campaigns:
            print(f"{dms_campaigns.index(campaign)+1}. Name: {campaign.campaign_name}")
        print(f"\n0. Go Back\n\nChoose the Campaign to cancel.")
        try:
            input_value = int(input("> "))
            if input_value > 0:
                dms_campaigns[input_value - 1].delete()
                clear_console()
                print("Campaign Deleted.", dungeon_master_.print_info())
            elif input_value == 0:
                clear_console()
                print("Cancelled action.")
        except IndexError or ValueError:
            clear_console()
            print("That's not a valid choice.")
    else:
        clear_console()
        print("Not running any Campaigns.")

def update_dm_modality(dungeon_master_, modality_int):
    if modality_int == 1:
        dungeon_master_.modality = "Online"
        dungeon_master_.update()
        clear_console()
        print(f"\n{dungeon_master_.name} is now conducting their sessions {dungeon_master_.modality}")
    elif modality_int == 2:
        dungeon_master_.modality = "In-Person"
        dungeon_master_.update()
        clear_console()
        print(f"\n{dungeon_master_.name} is now conducting their sessions {dungeon_master_.modality}")
    else:
        return ValueError

def list_dungeonmasters():
    dungeon_masters = DungeonMaster.get_all()
    print("\nDungeon Master List:\n")
    for dungeon_master in dungeon_masters:
        print(f"{dungeon_masters.index(dungeon_master)+1}. {dungeon_master.name}")
    return dungeon_masters

def delete_dungeon_master(dungeon_master_):
    for campaign in dungeon_master_.campaigns():
        campaign.delete()
    clear_console()
    print(f'\nDungeon Master {dungeon_master_.name} deleted.')
    dungeon_master_.delete()

def create_dungeon_master(dm_name: str, modality: int):
    if modality == 1:
        dm = DungeonMaster.create(dm_name, "Online")
        clear_console()
        print(f"\n{dm.name} is a new {dm.modality} Dungeon Master!")
    elif modality == 2:
        dm = DungeonMaster.create(dm_name, "In-Person")
        clear_console()
        print(f"\n{dm.name} is a new {dm.modality} Dungeon Master!")
    else:
        return ValueError


def exit_program():
    clear_console()
    print("\nGoodbye!\n")
    exit()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')