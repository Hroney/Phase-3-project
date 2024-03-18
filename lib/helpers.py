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
        print(f"{campaigns.index(campaign)+1}. {campaign.name}")
    return campaigns

def delete_campaign(campaign):
        clear_console()
        if campaign := Campaign.find_by_id(campaign.id):
            print(f'Campaign {campaign.name} deleted.')
            campaign.delete()
        else:
            clear_console()
            print(f"Campaign not deleted")

def update_campaign_name(campaign):
    clear_console()
    print("\nEnter Campaign's new name")
    campaign.name = input("> ")
    campaign.update()
    clear_console()
    print(f"\nCampaign Updated: {print_info_campaign(campaign)}")

def update_campaign_dm(campaign):
    clear_console()
    print("\nEnter New Dungeon Master")
    dungeon_masters = list_dungeonmasters()
    try:
        input_value = int(input("> "))
        if input_value >0:
            campaign.dungeon_master_id = dungeon_masters[input_value - 1].id
            campaign.update()
            clear_console()
            print("\nCampaign Updated: ", print_info_campaign(campaign))
        else:
            clear_console()
            print("Not a valid Dungeon Master")
    except IndexError or ValueError:
        clear_console()
        print("Not a valid Dungeon Master")


def create_a_campaign(dungeon_master):
    clear_console()
    print("\nWhat's the Name of the new campaign?")
    try:
        campaign = Campaign.create(input("> "), dungeon_master.id)
        clear_console()
        print(f"\n{campaign.name} has been created! Good luck!")
    except Exception as exc:
        clear_console()
        print("Error creating Campaign: ", exc, "\n")

def cancel_a_campaign(dungeon_master):
    clear_console()
    dms_campaigns = dungeon_master.campaigns()
    if len(dms_campaigns):
        print("\n\n\n\n")
        for campaign in dms_campaigns:
            print(f"{dms_campaigns.index(campaign)+1}. Name: {campaign.name}")
        print(f"\n0. Go Back\n\nChoose the Campaign to cancel.")
        try:
            input_value = int(input("> "))
            if input_value > 0:
                dms_campaigns[input_value - 1].delete()
                clear_console()
                print("Campaign Deleted.", print_info_dungeon_master(dungeon_master))
            elif input_value == 0:
                clear_console()
                print("Cancelled action.")
        except IndexError or ValueError:
            clear_console()
            print("That's not a valid choice.")
    else:
        clear_console()
        print("Not running any Campaigns.")

def update_dm_modality(dungeon_master, modality_int):
    if modality_int == 1:
        dungeon_master.modality = "Online"
        dungeon_master.update()
        clear_console()
        print(f"\n{dungeon_master.name} is now conducting their sessions {dungeon_master.modality}")
    elif modality_int == 2:
        dungeon_master.modality = "In-Person"
        dungeon_master.update()
        clear_console()
        print(f"\n{dungeon_master.name} is now conducting their sessions {dungeon_master.modality}")
    else:
        return ValueError

def list_dungeonmasters():
    dungeon_masters = DungeonMaster.get_all()
    print("\nDungeon Master List:\n")
    for dungeon_master in dungeon_masters:
        print(f"{dungeon_masters.index(dungeon_master)+1}. {dungeon_master.name}")
    return dungeon_masters

def delete_dungeon_master(dungeon_master):
    for campaign in dungeon_master.campaigns():
        campaign.delete()
    clear_console()
    print(f'\nDungeon Master {dungeon_master.name} deleted.')
    dungeon_master.delete()

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


def print_info_campaign(campaign):
    return f"Campaign Name: {campaign.name}, Dungeon Master: {DungeonMaster.find_by_id(campaign.dungeon_master_id).name}"

def print_info_dungeon_master(dungeon_master):
    campaigns_info = ", ".join(campaign.name for campaign in dungeon_master.campaigns())
    return f"Name: {dungeon_master.name}\nModality: {dungeon_master.modality}\nCampaigns: {campaigns_info}"