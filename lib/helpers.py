# lib/helpers.py
from models.campaign.Campaign import Campaign
from models.dungeon_master.Dungeon_Master import DungeonMaster
from models.player.Player import Player
from models.player_campaign.Player_Campaign import PlayerCampaign
import os



### Campaign Helpers ###

def list_campaigns():
    campaigns = Campaign.get_all()
    print("\n\nCampaign List:\n")
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
    print("Enter Campaign's new name")
    campaign_.campaign_name = input("> ")
    campaign_.update()
    clear_console()
    print(f"Campaign Updated: {campaign_.print_info()}\n")

def update_campaign_dm(campaign_):
    clear_console()
    print("Enter New Dungeon Master")
    dungeon_masters = list_dungeonmasters()
    try:
        input_value = int(input("> "))
        if input_value >0:
            campaign_.dungeon_master_id = dungeon_masters[input_value - 1].id
            campaign_.update()
            print("Campaign Updated: ", campaign_.print_info())
        else:
            clear_console()
            print("Not a valid Dungeon Master")
    except IndexError or ValueError:
        clear_console()
        print("Not a valid Dungeon Master")


def create_a_campaign(dungeon_master_):
    print("What's the Name of the new campaign?")
    try:
        campaign_ = Campaign.create(input("> "), dungeon_master_.id)
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
        print(f"\nChoose the Campaign to cancel.")
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
        print("Not in any Campaigns.")

def update_dm_modality(dungeon_master_, modality_int):
    if modality_int == 1:
        dungeon_master_.modality = "OnLine"
        dungeon_master_.update()
    elif modality_int == 2:
        dungeon_master_.modality = "In-Person"
        dungeon_master_.update()
    else:
        return ValueError

def list_dungeonmasters():
    dungeon_masters = DungeonMaster.get_all()
    print("\n\nDungeon Master List:\n")
    for dungeon_master in dungeon_masters:
        print(f"{dungeon_masters.index(dungeon_master)+1}. {dungeon_master.name}")
    return dungeon_masters



# def list_players_by_campaign():
#     print("Enter the Campaign's ID")
#     campaign_id_ = input("> ")
#     player_campaigns_ = PlayerCampaign.get_all()
#     if campaign_ := Campaign.find_by_id(campaign_id_):
#         clear_console()
#         for player_campaign_ in player_campaigns_:
#             if player_campaign_.campaign == int(campaign_id_):
#                 print(Player.find_by_id(int(player_campaign_.player)))
#     else:
#         clear_console()
#          print(f'Campaign {campaign_id_} not found.')

### Dungeon Master Helpers ###

# def find_by_name_dungeon_master():
#     print("Enter the name of the Dungeon Master")
#     dungeon_master_ = input("> ")
#     clear_console()
#     dungeonmaster = DungeonMaster.find_by_name(dungeon_master_)
#     print(dungeonmaster) if dungeonmaster else print (f'{dungeon_master_} is not found.')

# def find_by_id_dungeon_master():
#     print("Enter the ID of the Dungeon Master")
#     dungeon_master_id_ = input("> ")
#     clear_console()
#     dungeon_master_ = DungeonMaster.find_by_id(dungeon_master_id_)
#     print(dungeon_master_) if dungeon_master_ else print (f'Dungeon Master ID: {dungeon_master_id_} not found.')

# def create_dungeon_master():
#     print("Enter Dungeon Master's name")
#     dungeon_master_name_ = input("> ")
#     dungeon_master_modality_ = modality_menu()
#     clear_console()
#     try:
#         dungeonmaster_ = DungeonMaster.create(dungeon_master_name_, dungeon_master_modality_)
#     except Exception as exc:
#         print("Error creating Dungeon Master: ", exc, "\n")
#     if dungeonmaster_ is not None:
#         print(f"success: {dungeonmaster_} \n")
#     else:
#         print(f'Error: Dungeon Master not created.\n')

# def update_dungeon_master():
#     print("Enter the ID of the Dungeon Master")
#     dungeon_master_id_ = input("> ")
#     if dungeonmaster_ := DungeonMaster.find_by_id(dungeon_master_id_):
#         clear_console()
#         print(f'{dungeonmaster_}')
#         try:
#             updatemenu_dungeon_master()
#             update_choice_ = input("> ")
#             if update_choice_ == "1":
#                 print("Enter Dungeon Master's new name")
#                 dungeon_master_name_ = input("> ")
#                 dungeonmaster_.name = dungeon_master_name_
#                 dungeonmaster_.update()
#                 clear_console()
#                 print(f'Success: {dungeonmaster_}\n')
#             elif update_choice_ == "2":
#                 print("Enter Dungeon Master's new modality")
#                 dungeon_master_modality_ = modality_menu()
#                 dungeonmaster_.modality = dungeon_master_modality_
#                 dungeonmaster_.update()
#                 clear_console()
#                 print(f'Success: {dungeonmaster_}\n')
#             elif update_choice_ == "3":
#                 print("Enter Dungeon Master's new name")
#                 dungeon_master_name_ = input("> ")
#                 dungeonmaster_.name = dungeon_master_name_
#                 print("Enter Dungeon Master's new modality")
#                 dungeon_master_modality_ = modality_menu()
#                 dungeonmaster_.modality = dungeon_master_modality_
#                 dungeonmaster_.update()
#                 clear_console()
#                 print(f'Success: {dungeonmaster_}\n')
#             else:
#                 clear_console()
#         except Exception as exc:
#             clear_console()
#             print("Error updating Dungeon Master: ", exc, "\n")
#     else:
#         clear_console()
#         print(f'Dungeon Master {dungeon_master_id_} not found.\n')

# def updatemenu_dungeon_master():
#     print("\n________Update_Menu________")
#     print("Please select what to update.\n")
#     print("1. Name")
#     print("2. Modality")
#     print("3. Both")
#     print("\n0. Go Back")
#     print("___________________________")

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

# def list_campaigns_by_dungeon_master():
#     print("Enter the ID of the Dungeon Master")
#     dungeon_master_id_ = input("> ")
#     campaigns_ = Campaign.get_all()
#     atleastone = 0
#     clear_console()
#     if dungeon_master_id_.isnumeric():
#         for campaign_ in campaigns_:
#             if int(campaign_.dungeon_master_id) == int(dungeon_master_id_):
#                 print(campaign_)
#                 atleastone += 1
#         if atleastone == 0:
#             if DungeonMaster.find_by_id(dungeon_master_id_):
#                 print(f"No Campaigns found for {DungeonMaster.find_by_id(dungeon_master_id_).name}")
#             else:
#                 print(f"{dungeon_master_id_} is not a valid dungeon master ID")

### Player Helpers ###
                
# def campaign_list(player):
#     player_campaigns_ = PlayerCampaign.get_all()
#     returnstring = "     Campaigns: "
#     for player_campaign in player_campaigns_:
#         if player_campaign.player == player.id:
#             returnstring += f"{Campaign.find_by_id(player_campaign.campaign).campaign_name}, "
#     if returnstring == "     Campaigns: ":
#         return "     Not in a Campaign."
#     return returnstring[:-2]

# def list_players():
#     players = Player.get_all()
#     clear_console()
#     for player in players:
#         print(player)
#         print(campaign_list(player),f"\n")


# def find_by_name_player():
#     print("Enter the name of the Player")
#     player_ = input("> ")
#     clear_console()
#     player = Player.find_by_name(player_)
#     print(player) if player else print (f'{player_} is not found.')

# def find_by_id_player():
#     print("Enter the ID of the Player")
#     player_id_ = input("> ")
#     clear_console()
#     player_ = Player.find_by_id(player_id_)
#     print(player_) if player_ else print (f'Player ID: {player_id_} not found.')

# def create_player():
#     print("Enter Player's name")
#     player_name_ = input("> ")
#     print("Enter Player's Email address")
#     player_email_ = input("> ")
#     clear_console()
#     try:
#         if player_ := Player.create(player_name_, player_email_):
#             print(f"success: {player_} \n") 
#     except Exception as exc:
#         print("Error creating Player: ", exc, "\n")


# def updatemenu_player():
#     print("\n________Update_Menu________")
#     print("Please select what to update.\n")
#     print("1. Name")
#     print("2. Email")
#     print("3. Both")
#     print("\n0. Go Back")
#     print("___________________________")

# def update_player():
#     print("Enter the ID of the Player")
#     player_id_ = input("> ")
#     if player_ := Player.find_by_id(player_id_):
#         clear_console()
#         print(f'{player_}')
#         try:
#             updatemenu_player()
#             update_choice_ = input("> ")
#             if update_choice_ == "1":
#                 print("Enter Player's new name")
#                 player_name_ = input("> ")
#                 player_.name = player_name_
#                 player_.update()
#                 clear_console()
#                 print(f'Success: {player_}\n')
#             elif update_choice_ == "2":
#                 print("Enter Player's new Email")
#                 player_email_ = input("> ")
#                 player_.email = player_email_
#                 player_.update()
#                 clear_console()
#                 print(f'Success: {player_}\n')
#             elif update_choice_ == "3":
#                 print("Enter Player's new name")
#                 player_name_ = input("> ")
#                 player_.name = player_name_
#                 print("Enter Player's new Email")
#                 player_email_ = input("> ")
#                 player_.email = player_email_
#                 player_.update()
#                 clear_console()
#                 print(f'Success: {player_}\n')
#             else:
#                 clear_console()
#         except Exception as exc:
#             clear_console()
#             print("Error updating Player: ", exc, "\n")
#     else:
#         clear_console()
#         print(f'Player {player_id_} not found.\n')

# def delete_player():
#     print("Enter the Player's id")
#     player_id_ = input("> ")
#     if player_ := Player.find_by_id(player_id_):
#         player_campaigns_ = PlayerCampaign.get_all()
#         for player_campaign in player_campaigns_:
#             if player_campaign.player == int(player_id_):
#                 player_campaign.delete()
#         player_.delete()
#         clear_console()
#         print(f'Player {player_id_} deleted.')
#     else:
#         clear_console()
#         print(f'Player {player_id_} not found.')

# def add_campaign():
#     print("Enter the ID of the Player")
#     player_id_ = input("> ")
#     print("Enter the ID of the Campaign")
#     campaign_id_ = input("> ")
#     clear_console()
#     try:
#         if player_campaign_ := PlayerCampaign.create(int(player_id_), int(campaign_id_)):
#             print(f"{Player.find_by_id(player_id_).name} has joined {Campaign.find_by_id(campaign_id_).campaign_name}")
#     except Exception as exc:
#         print("Raised Exception, ", exc)


# def leave_campaign():
#     print("Enter the ID of the Player")
#     player_id_ = input("> ")
#     clear_console()
#     player_campaigns_ = PlayerCampaign.get_all()
#     if player_id_.isnumeric():
#         for player_campaign_ in player_campaigns_:
#             if player_campaign_.player == int(player_id_):
#                 print(Campaign.find_by_id(player_campaign_.campaign))
#         print("\nEnter the ID of the Campaign you wish to leave")
#         delete_choice_ = input("> ")
#         for player_campaign_ in player_campaigns_:
#             if (player_campaign_.player == int(player_id_)) and (player_campaign_.campaign == int(delete_choice_)):
#                 player_campaign_.delete()
#         clear_console()
#         print(f"{Player.find_by_id(int(player_id_)).name} left {Campaign.find_by_id(int(delete_choice_)).campaign_name}")

# def list_campaign_by_player():
#     print("Enter the ID of the Player")
#     player_id_ = input("> ")
#     clear_console()
#     player_campaigns_ = PlayerCampaign.get_all()
#     campaigns_ = Campaign.get_all()
#     at_least_one_ = 0
#     if player_id_.isnumeric():
#         for player_campaign_ in player_campaigns_:
#             if player_campaign_.player == int(player_id_):
#                 print(Campaign.find_by_id(player_campaign_.campaign))
#                 at_least_one_ += 1
#     else:
#         print(f"{player_id_} is not a valid ID number")
#     if at_least_one_ == 0:
#         if Player.find_by_id(player_id_) is not None:
#             print(f"Player {Player.find_by_id(player_id_).name} is not part of a Campaign.")
#         else:
#             print(f"Not a Valid Player ID")


def exit_program():
    print("Goodbye!")
    exit()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')