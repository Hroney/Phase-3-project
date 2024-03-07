# lib/helpers.py
from models.campaign.Campaign import Campaign
from models.dungeon_master.Dungeon_Master import DungeonMaster
import os



### Campaign Helpers ###
def list_campaigns():
    campaigns = Campaign.get_all()
    for campaign in campaigns:
        print(campaign)
    print("\n")

def create_campaign():
    campaign_name_ = input("Enter campaign name: ")
    dungeon_master_ = int(input("Enter Dungeon Master's ID number: "))
    try:
        campaign_ = Campaign.create(campaign_name_, dungeon_master_)
    except Exception as exc:
        print("Error creating Campaign: ", exc, "\n")
    if campaign_ is not None:
        print(f"success: {campaign_} \n")
    else:
        print(f'Error: Campaign not created. Dungeon Master not in Database. \n')

def find_by_name_campaign():
    campaign_name_ = input("Enter the name of the Campaign: ")
    campaign = Campaign.find_by_name(campaign_name_)
    print(campaign) if campaign else print (f'{campaign_name_} is not found.')
    print("\n")

def find_by_id_campaign():
    campaign_id_ = input("Enter the ID of the Campaign: ")
    campaign_ = Campaign.find_by_id(campaign_id_)
    print(campaign_) if campaign_ else print (f'Campaign {campaign_id_} not found.')
    print("\n")

def update_campaign():
    campaign_id_ = input("Enter the ID of the Campaign: ")
    if campaign := Campaign.find_by_id(campaign_id_):
        print(f'{campaign}')
        try:
            updatemenu()
            update_choice_ = input("> ")
            if update_choice_ == "1":
                print("Enter Campaign's new name")
                campaign_name_ = input("> ")
                campaign.campaign_name = campaign_name_
                campaign.update()
                clear_console()
                print(f'Success: {campaign}\n')
            elif update_choice_ == "2":
                print("Enter Campaign's new Dungeon Master ID")
                campaign_dm_ = input("> ")
                if DungeonMaster.find_by_id(campaign_dm_):
                    campaign.dungeon_master_id = campaign_dm_
                    campaign.update()
                    clear_console()
                    print(f'Success: {campaign}\n')
                else:
                    clear_console()
                    print(f'{campaign_dm_} is not a valid Dungeon Master\n')
            elif update_choice_ == "3":
                print("Enter Campaign's new name")
                campaign_name_ = input("> ")
                campaign.campaign_name = campaign_name_
                print("Enter Campaign's new Dungeon Master ID")
                campaign_dm_ = input("> ")
                if DungeonMaster.find_by_id(campaign_dm_):
                    campaign.dungeon_master_id = campaign_dm_
                    campaign.update()
                    clear_console()
                    print(f'Success: {campaign}\n')
                else:
                    clear_console()
                    print(f'{campaign_dm_} is not a valid Dungeon Master\n')
            else:
                clear_console()
        except Exception as exc:
            clear_console()
            print("Error updating Campaign: ", exc, "\n")
    else:
        clear_console()
        print(f'Campaign {campaign_id_} not found.\n')
    

def updatemenu():
    print("\n________Update_Menu________")
    print("Please select what to update.\n")
    print("1. Campaign Name")
    print("2. Dungeon Master")
    print("3. Both")
    print("\n4. Go Back")
    print("___________________________")























def exit_program():
    print("Goodbye!")
    exit()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')