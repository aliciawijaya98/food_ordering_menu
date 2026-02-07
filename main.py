from menu_management import view_menu, add_item, edit_delete_item, search_menu
from order_management import order_type, show_orders
from menu_database import get_menu

def main_menu():
    while True:
        print ("=== RestoApps ===")
        print ("1. Menu Management")
        print ("2. Order Management")
        print ("3. Exit program")

        user_input = int(input("Choose between 1-3: "))

        if user_input == 1:
            menu_management() 
        elif user_input == 2: 
            order_management()
        elif user_input == 3: 
            print("Session ended")
        else: 
            print("Invalid option. Please choose 1-3.")

def menu_management():
    while True:
        print("=== MANAGE MENU ===")
        print("1. View full menu")
        print("2. Add new menu item")
        print("3. Edit/delete item on the menu")
        print("4. Search menu")
        print("5. Exit program")

        user_input = int(input("Choose between 1-5: "))

        if user_input == 1:
            view_menu(get_menu(), allow_edit=True)
        elif user_input == 2:
            add_item()
        elif user_input == 3:
            edit_delete_item(get_menu())
        elif user_input == 4: 
            search_menu()
        elif user_input == 5:
            print("\nSession ended.")
            break
        else:
            print("Invalid option. Please choose 1-5.")

def order_management():
    while True:
        print("\n--- ORDER MENU ---")
        print("1. Take order")
        print("2. Review order")
        print("3. Exit program")
    
        try:
            user_input = int(input("Choose between 1-3: "))
        except ValueError:
            print("Must be a number. Try again.")
            continue

        if user_input == 1:
            order_type()
        elif user_input == 2:
            table_or_invoice = input("Enter table number or invoice to review: ").strip()
            show_orders(table_or_invoice)
        elif user_input == 3:
            print("\nSession ended.")
            break
        else:
            print("Invalid option. Please choose 1-5.")

#menentukan apakah file main dipanggil atau tidak
if __name__ == "__main__":
    main_menu()