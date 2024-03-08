# lib/helpers.py
from models.campaign.Campaign import Campaign
from models.dungeon_master.Dungeon_Master import DungeonMaster
import os



### Campaign Helpers ###
def list_campaigns():
    campaigns = Campaign.get_all()
    clear_console()
    for campaign in campaigns:
        print(campaign)

def create_campaign():
    print("Enter campaign name")
    campaign_name_ = input("> ")
    print("Enter Dungeon Master's ID number")
    dungeon_master_ = int(input("> "))
    clear_console()
    try:
        campaign_ = Campaign.create(campaign_name_, dungeon_master_)
    except Exception as exc:
        print("Error creating Campaign: ", exc, "\n")
    if campaign_ is not None:
        print(f"success: {campaign_} \n")
    else:
        print(f'Error: Campaign not created. Dungeon Master not in Database. \n')

def find_by_name_campaign():
    print("Enter the name of the Campaign")
    campaign_name_ = input("> ")
    clear_console()
    campaign = Campaign.find_by_name(campaign_name_)
    print(campaign) if campaign else print (f'{campaign_name_} is not found.')

def find_by_id_campaign():
    print("Enter the ID of the Campaign")
    campaign_id_ = input("> ")
    clear_console()
    campaign_ = Campaign.find_by_id(campaign_id_)
    print(campaign_) if campaign_ else print (f'Campaign {campaign_id_} not found.')

def update_campaign():
    print("Enter the ID of the Campaign")
    campaign_id_ = input("> ")
    if campaign := Campaign.find_by_id(campaign_id_):
        clear_console()
        print(f'{campaign}')
        try:
            updatemenu_campaign()
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
    

def updatemenu_campaign():
    print("\n________Update_Menu________")
    print("Please select what to update.\n")
    print("1. Campaign Name")
    print("2. Dungeon Master")
    print("3. Both")
    print("\n0. Go Back")
    print("___________________________")

def delete_campaign():
    print("Enter the Campaign's id")
    campaign_id_ = input("> ")
    if campaign_ := Campaign.find_by_id(campaign_id_):
        campaign_.delete()
        clear_console()
        print(f'Campaign {campaign_id_} deleted.')
    else:
        clear_console()
        print(f'Campaign {campaign_id_} not found.')


### Dungeon Master Helpers ###
def list_dungeonmasters():
    dungeon_masters = DungeonMaster.get_all()
    clear_console()
    for dungeon_master in dungeon_masters:
        print(dungeon_master)

def find_by_name_dungeon_master():
    print("Enter the name of the Dungeon Master")
    dungeon_master_ = input("> ")
    clear_console()
    dungeonmaster = DungeonMaster.find_by_name(dungeon_master_)
    print(dungeonmaster) if dungeonmaster else print (f'{dungeon_master_} is not found.')

def find_by_id_dungeon_master():
    print("Enter the ID of the Dungeon Master")
    dungeon_master_id_ = input("> ")
    clear_console()
    dungeon_master_ = DungeonMaster.find_by_id(dungeon_master_id_)
    print(dungeon_master_) if dungeon_master_ else print (f'Dungeon Master ID: {dungeon_master_id_} not found.')

def modality_menu():
    print("___________________________")
    print("Select option of Modality")
    print("(Defaults to Undefined)")
    print("1. Online")
    print("2. In-person")
    dungeon_master_modality_ = int(input("> "))
    if dungeon_master_modality_ == 1:
        return "Online"     
    elif dungeon_master_modality_ == 2:
        return "In-person"
    else:
        return "Undefined"

def create_dungeon_master():
    print("Enter Dungeon Master's name")
    dungeon_master_name_ = input("> ")
    dungeon_master_modality_ = modality_menu()
    clear_console()
    try:
        dungeonmaster_ = DungeonMaster.create(dungeon_master_name_, dungeon_master_modality_)
    except Exception as exc:
        print("Error creating Dungeon Master: ", exc, "\n")
    if dungeonmaster_ is not None:
        print(f"success: {dungeonmaster_} \n")
    else:
        print(f'Error: Dungeon Master not created.\n')

def update_dungeon_master():
    print("Enter the ID of the Dungeon Master")
    dungeon_master_id_ = input("> ")
    if dungeonmaster_ := DungeonMaster.find_by_id(dungeon_master_id_):
        clear_console()
        print(f'{dungeonmaster_}')
        try:
            updatemenu_dungeon_master()
            update_choice_ = input("> ")
            if update_choice_ == "1":
                print("Enter Dungeon Master's new name")
                dungeon_master_name_ = input("> ")
                dungeonmaster_.name = dungeon_master_name_
                dungeonmaster_.update()
                clear_console()
                print(f'Success: {dungeonmaster_}\n')
            elif update_choice_ == "2":
                print("Enter Dungeon Master's new modality")
                dungeon_master_modality_ = modality_menu()
                dungeonmaster_.modality = dungeon_master_modality_
                dungeonmaster_.update()
                clear_console()
                print(f'Success: {dungeonmaster_}\n')
            elif update_choice_ == "3":
                print("Enter Dungeon Master's new name")
                dungeon_master_name_ = input("> ")
                dungeonmaster_.name = dungeon_master_name_
                print("Enter Dungeon Master's new modality")
                dungeon_master_modality_ = modality_menu()
                dungeonmaster_.modality = dungeon_master_modality_
                dungeonmaster_.update()
                clear_console()
                print(f'Success: {dungeonmaster_}\n')
            else:
                clear_console()
        except Exception as exc:
            clear_console()
            print("Error updating Dungeon Master: ", exc, "\n")
    else:
        clear_console()
        print(f'Campaign {dungeon_master_id_} not found.\n')

def updatemenu_dungeon_master():
    print("\n________Update_Menu________")
    print("Please select what to update.\n")
    print("1. Name")
    print("2. Modality")
    print("3. Both")
    print("\n0. Go Back")
    print("___________________________")

def delete_dungeon_master():
    print("___________________________")
    print("Deleting a Dungeon Master deletes")
    print("all Campaigns they are in charge of")
    print("Press 0 to back out.")
    print("___________________________")
    print("Enter the Dungeon Master's id")
    dungeon_master_id_ = input("> ")
    if dungeon_master_id_ == "0":
        clear_console()
    elif dungeon_master_ := DungeonMaster.find_by_id(dungeon_master_id_):
        campaigns_ = Campaign.get_all()
        for campaign in campaigns_:
            if int(campaign.dungeon_master_id) == int(dungeon_master_id_):
                while True:
                    print(f"Is another Dungeon Master taking over {campaign.campaign_name}?")
                    print("Respond 'yes' or 'no'.")
                    choice_ = input("> ")
                    if choice_.lower() == "yes":
                        print("Please enter the ID of the replacement Dungeon Master")
                        choice_id_ = input("> ")
                        if DungeonMaster.find_by_id(choice_id_):
                            campaign.dungeon_master_id = choice_id_
                            campaign.update()
                            print(f'Success: {campaign}\n')
                            break
                        else:
                            print(f'{choice_id_} is not a valid Dungeon Master\n')
                    elif choice_.lower() == "no":
                        print(f"Campaign {campaign.campaign_name} is being deleted.")
                        campaign.delete()
                        break
                    else:
                        print("invalid choice.")
        dungeon_master_.delete()
        clear_console()
        print(f'Dungeon Master {dungeon_master_id_} deleted.')
    else:
        clear_console()
        print(f'Dungeon Master {dungeon_master_id_} not found.')








def exit_program():
    print("Goodbye!")
    exit()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')