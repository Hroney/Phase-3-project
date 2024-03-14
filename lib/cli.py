# lib/cli.py

from helpers import (
    exit_program,
    clear_console,
    list_campaigns,
    list_dungeonmasters,
    delete_campaign,
    update_campaign_name,
    update_campaign_dm,
    delete_dungeon_master,
    create_a_campaign,
    cancel_a_campaign,
    update_dm_modality,
    
)

### Main Menu ###

def main():
    while True:
        clear_console()
        main_menu()
        main_choice = input("> ")
        if main_choice == "0":
            exit_program()
        elif main_choice == "1":
            clear_console()
            print()
            campaign_menu_choice()
        elif main_choice == "2":
            clear_console()
            print()
            dungeon_master_menu_choice()
        elif main_choice == "3":
            clear_console()
            player_menu_choice()
        else:
            print("Invalid choice")


def main_menu():
    print("\n\n\nMain Menu:\n")
    print("1. Campaign List")
    print("2. Dungeon Master List")
    print("3. Player Menu")
    print("4. Creation List")
    print("\n0. Exit the program\n")
    print("Please select an option:")
    

### Campaign Menu ###

def campaign_menu():
    print("\n\n1. Change Campaign Name")
    print("2. Change Campaign Ownership")
    print("3. End Campaign")
    print("\n0. Go Back\n")
    print("Please select an option:")
    

def campaign_menu_choice():
    while True:
        campaigns = list_campaigns()
        if len(campaigns):
            print("\n0. Main Menu")
            print("\nPlease select a Campaign:")
            try:
                input_choice = int(input("> "))
                clear_console()
                if input_choice == 0:
                    break
                if type(input_choice) == int:
                    try:
                        campaign_choice = campaigns[input_choice-1]
                        print(f"\n{campaign_choice.print_info()}")
                        campaign_menu()
                        menu_choice = input("> ")
                        while True:
                            if menu_choice == "0":
                                clear_console()
                                print()
                                break
                            elif menu_choice == "1":
                                update_campaign_name(campaign_choice)
                                break
                            elif menu_choice == "2":
                                update_campaign_dm(campaign_choice)
                                break
                            elif menu_choice == "3":
                                delete_campaign(campaign_choice)
                                break
                            else:
                                print("That's not a valid choice.")
                                break
                    except IndexError:
                        print("Not a valid choice.")
            except ValueError:
                print("Not a valid choice.")
        else:
            print("There are No Campaigns")
            break

### Dungeon Master Menu ###

def dungeon_master_menu():
    print("\n1. Start a new Campaign")
    print("2. Cancel a Campaign")
    print("3. Change modality")
    print("\n0. Go Back\n")
    print("Please select an option:")

def dungeon_master_menu_choice():
    while True:
        dungeon_masters = list_dungeonmasters()
        if len(dungeon_masters):
            print("\n0. Main Menu")
            print("\nPlease select a Dungeon Master:")
            try:
                input_choice = int(input("> "))
                clear_console()
                if input_choice == 0:
                    break
                if type(input_choice) == int:
                    try:
                        dungeon_master_choice = dungeon_masters[input_choice-1]
                        print(f"\n{dungeon_master_choice.print_info()}")
                        dungeon_master_menu()
                        menu_choice = input("> ")
                        while True:
                            if menu_choice == "0":
                                clear_console()
                                print()
                                break
                            elif menu_choice == "1":
                                create_a_campaign(dungeon_master_choice)
                                break
                            elif menu_choice == "2":
                                cancel_a_campaign(dungeon_master_choice)
                                break
                            elif menu_choice == "3":
                                print("1. Online\n2.In-Person\n\n0. Go Back")
                                try:
                                    modality_int = int(input("> "))
                                    if modality_int == 0:
                                        break
                                    update_dm_modality(dungeon_master_choice, modality_int)
                                except ValueError:
                                    print("That's not a valid choice.")
                                break
                            else:
                                print("That's not a valid choice.")
                                break
                    except IndexError:
                        print("Not a valid choice.")
            except ValueError:
                print("That's not a valid choice.")
            



### Player Menu ###
    
def player_menu_choice():
    list_players()
    while True:
        player_menu()
        player_choice = input("> ")
        if player_choice == "0":
            break



def player_menu():
    print("\n_______Player_Menu_______")
    print("  Please select an option:\n")

    print("\n0. Go Back to Main Menu")
    print("___________________________")


if __name__ == "__main__":
    main()
