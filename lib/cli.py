# lib/cli.py

from helpers import (
    exit_program,
    clear_console,
    list_campaigns,
    create_campaign,
    find_by_name_campaign,
    find_by_id_campaign,
    update_campaign,
    delete_campaign,
    list_dungeonmasters,
    find_by_id_dungeon_master,
    find_by_name_dungeon_master,
    create_dungeon_master,
    update_dungeon_master,
    delete_dungeon_master,
    list_campaigns_by_dungeon_master
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
            campaign_menu_choice()
        elif main_choice == "2":
            clear_console()
            dungeon_master_menu_choice()
                    
        else:
            print("Invalid choice")


def main_menu():
    print("\n_________Main_Menu_________")
    print("  Please select an option:\n")
    print("1. Campaign Menu")
    print("2. Dungeon Master Menu")

    print("\n0. Exit the program")
    print("___________________________")

### Campaign Menu ###
def campaign_menu_choice():
    while True:
        campaign_menu()
        campaign_choice = input("> ")
        if campaign_choice == "0":
            break
        elif campaign_choice == "1":
            list_campaigns()
        elif campaign_choice == "2":
            find_by_name_campaign()
        elif campaign_choice == "3":
            find_by_id_campaign()
        elif campaign_choice == "4":
            create_campaign()
        elif campaign_choice == "5":
            update_campaign()
        elif campaign_choice == "6":
            delete_campaign()

        else:
            clear_console()

def campaign_menu():
    print("\n_______Campaign_Menu_______")
    print("  Please select an option:\n")
    print("1. List all Campaign's")
    print("2. Find Campaign by Name")
    print("3. Find Campaign by ID")
    print("4. Create a new Campaign")
    print("5. Update Campaign")
    print("6. Delete Campaign")

    print("\n0. Go back to Main Menu")
    print("___________________________")

### Dungeon Master Menu ###

def dungeon_master_menu_choice():
    while True:
        dungeon_master_menu()
        dungeon_master_choice = input("> ")
        if dungeon_master_choice == "0":
            break
        elif dungeon_master_choice == "1":
            list_dungeonmasters()
        elif dungeon_master_choice == "2":
            find_by_name_dungeon_master()
        elif dungeon_master_choice == "3":
            find_by_id_dungeon_master()
        elif dungeon_master_choice == "4":
            create_dungeon_master()
        elif dungeon_master_choice == "5":
            update_dungeon_master()
        elif dungeon_master_choice == "6":
            delete_dungeon_master()
        elif dungeon_master_choice == "7":
            list_campaigns_by_dungeon_master()
        
        else:
            clear_console()
        
        

def dungeon_master_menu():
    print("\n____Dungeon_Master_Menu____")
    print("  Please select an option:\n")
    print("1. List all Dungeon Masters")
    print("2. Find Dungeon Master by Name")
    print("3. Find Dungeon Master by ID")
    print("4. Create Dungeon Master")
    print("5. Update Dungeon Master")
    print("6. Delete Dungeon Master")
    print("7. Find Campaigns by Dungeon Master")

    print("\n0. Go Back to Main Menu")
    print("___________________________")


if __name__ == "__main__":
    main()
