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
    create_dungeon_master
)

### Main Menu ###

def main():
    clear_console()
    print("\n")
    while True:
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
            print()
            register_as_dungeon_master()
        else:
            clear_console()
            print("\nInvalid choice")


def main_menu():
    print("\nMain Menu:\n")
    print("1. Campaign(s)")
    print("2. Dungeon Master(s)")
    print("3. Register a new Dungeon Master")
    print("\n0. Exit the program\n")
    print("Please select an option:")
    

### Campaign Menu ###

def campaign_menu():
    print("\n\n\n1. Change Campaign Name")
    print("2. Change Campaign Ownership")
    print("3. End Campaign")
    print("\n0. Go Back\n")
    print("Please select an option:")
    

def campaign_menu_choice():
    print()
    while True:
        campaigns = list_campaigns()
        if len(campaigns):
            print("\n0. Main Menu")
            print("\nPlease select a Campaign:")
            try:
                input_choice = int(input("> "))
                clear_console()
                if input_choice == 0:
                    print("\n")
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
                                print("\n")
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
            clear_console()
            print("\nThere are No Campaigns.")
            break

### Dungeon Master Menu ###

def dungeon_master_menu():
    print("\n1. Start a new Campaign")
    print("2. Cancel a Campaign")
    print("3. Change between Online / In-person")
    print("4. QUIT!")
    print("\n0. Go Back\n")
    print("Please select an option:")

def dungeon_master_menu_choice():
    print()
    while True:
        dungeon_masters = list_dungeonmasters()
        if len(dungeon_masters):
            print("\n0. Main Menu")
            print("\nPlease select a Dungeon Master:")
            try:
                input_choice = int(input("> "))
                clear_console()
                if input_choice == 0:
                    print("\n")
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
                                print("\n")
                                break
                            elif menu_choice == "1":
                                create_a_campaign(dungeon_master_choice)
                                break
                            elif menu_choice == "2":
                                cancel_a_campaign(dungeon_master_choice)
                                break
                            elif menu_choice == "3":
                                clear_console()
                                print("\n\n\n\n\n1. Online\n2. In-Person\n\n0. Go Back")
                                print("\nPlease select an option:")
                                try:
                                    modality_int = int(input("> "))
                                    if modality_int == 0:
                                        clear_console()
                                        print("\nCancelled action")
                                        break
                                    update_dm_modality(dungeon_master_choice, modality_int)
                                except ValueError:
                                    print("That's not a valid choice.")
                                break
                            elif menu_choice == "4":
                                clear_console()
                                print("\n!! This cancels all of the Dungeon Masters Campaigns !!")
                                print("\nAre you sure? (yes or no)")
                                input_choice_ = input("> ")
                                if input_choice_.lower() == "yes":
                                    delete_dungeon_master(dungeon_master_choice)
                                    break
                                else:
                                    clear_console()
                                    print("\nNot a valid choice")
                                    break
                            else:
                                print("That's not a valid choice.")
                                break
                    except IndexError:
                        print("Not a valid choice.")
            except ValueError:
                print("That's not a valid choice.")
        else:
            clear_console()
            print("\nThere are No Dungeon Masters.")
            break

def register_as_dungeon_master():
    while True:
        print("What's the Dungeon Masters name?")
        dm_name = input("> ")
        print(f"\nIs {dm_name} hosting Online or In-person sessions?")
        print("\nPlease select an option:")
        print("\n1. Online")
        print("2. In-Person")
        try:
            modality_int_ = int(input("> "))
            if modality_int_ == 0:
                clear_console()
                print("\nCancelled Registration.")
                break
            create_dungeon_master(dm_name, modality_int_)
        except ValueError:
            print("That's not a valid choice.")
        break

if __name__ == "__main__":
    main()
