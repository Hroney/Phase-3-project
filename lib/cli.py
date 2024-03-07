# lib/cli.py

from helpers import (
    exit_program,
    clear_console,
    list_campaigns,
    create_campaign,
    find_by_name_campaign,
    find_by_id_campaign,
    update_campaign
)


def main():
    while True:
        clear_console()
        main_menu()
        main_choice = input("> ")

        if main_choice == "0":
            exit_program()
        elif main_choice == "1":
            clear_console()
            while True:
                campaign_menu()
                campaign_choice = input("> ")

                if campaign_choice == "0":
                    break
                elif campaign_choice == "1":
                    clear_console()
                    list_campaigns()
                elif campaign_choice == "2":
                    clear_console()
                    find_by_name_campaign()
                elif campaign_choice == "3":
                    clear_console()
                    find_by_id_campaign()
                elif campaign_choice == "4":
                    clear_console()
                    create_campaign()
                elif campaign_choice == "5":
                    clear_console()
                    update_campaign()
                    
        else:
            print("Invalid choice")


def main_menu():
    print("_________Main_Menu_________")
    print("Please select an option:\n")
    print("1. Campaign Menu")
    print("\n0. Exit the program")
    print("___________________________")

def campaign_menu():
    print("_______Campaign_Menu_______")
    print("Please select an option:\n")
    print("1. List all Campaign's")
    print("2. Find Campaign by Name")
    print("3. Find Campaign by ID")
    print("4. Create a new Campaign")
    print("5. Update Campaign")
    print("\n0. Go back to Main Menu")
    print("___________________________")

if __name__ == "__main__":
    main()
