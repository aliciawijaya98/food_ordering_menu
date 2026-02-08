from menu_database import get_menu, add_menu_item, menu_list

#View the menu
def view_menu(menu_dict, allow_edit=False):
    column_width = "{:<5} | {:<20} | {:<55} | {:<10}"
    header = column_width.format("No.", "Category","Item" , "Price")
    print(header)
    print("-" * len(header))

    for i, item in enumerate(menu_dict, start=1):
        price_format = f"Rp{item['price']:,}".replace(",",".")
        print(column_width.format(i, item["category"], item["item"], price_format))

    if allow_edit:
        while True:
            edit_choice = input("Do you want to edit/delete an item? (y/n): ")
            if edit_choice == "y":
                edit_delete_item(menu_dict)
                break
            elif edit_choice == "n":
                break
            else: 
                print("Please type 'y' or 'n'")


#Search the menu
def search_menu(menu_dict):
    while True:
        query = input("Search by category or item (or type 'q' to quit): ").strip().lower()
        
        if query == "q":
            print ("Exiting search...")
            break 

        filtered = [item for item in menu_dict 
                    if query in item["category"].lower() 
                    or query in item["item"].lower()] 
    
        if filtered:
            print(f"\nFound {len(filtered)} item(s) matching '{query}':")
            view_menu(filtered)
            # Ask if user wants to edit/delete filtered items
            edit_choice = input("Do you want to edit/delete these items? (y/n): ").strip().lower()
            if edit_choice == "y":
                edit_delete_item(filtered)
                break
            elif edit_choice == "n":
                break
            else: 
                print("Please type 'y' or 'n'")
        else:
            print(f"No items found matching '{query}'. Try again.")

#Edit or delete item
def edit_delete_item(menu_dict):
    if not menu_dict:
        print("No items available to edit/delete.")
        return
    
    view_menu(menu_dict)

    delete_index = input("Enter the index of the item to edit/delete (or 'q' to quit): ").strip()
    if delete_index.lower() == "q":
        return
    elif not delete_index.isdigit() or int(delete_index) < 1 or int(delete_index) >  len(menu_dict):
        print("Invalid index.")
        return

    selected_item = menu_dict[int(delete_index) - 1]
    print(f"Selected: {selected_item['item']}")

    edit_choice = input("Type 'e' to edit, 'd' to delete: ").strip().lower()

    if edit_choice == "e":
        new_category = input(f"New category (Enter to keep '{selected_item['category']}'): ").strip()
        new_name = input(f"New item name (Enter to keep '{selected_item['item']}'): ").strip()
        new_price = input(f"New price (Enter to keep '{selected_item['price']}'): ").strip()

        if new_category:
            selected_item["category"] = new_category
        if new_name:
            selected_item["item"] = new_name
        if new_price:
            try:
                selected_item["price"] = int(new_price)
            except ValueError:
                print("Invalid price. Keeping old value.")

        print("Item updated successfully!")

    elif edit_choice == "d":
        confirm = input(
            f"Are you sure you want to delete '{selected_item['item']}'? (y/n): "
        ).strip().lower()

        if confirm == "y":
            try:
                menu_list.remove(selected_item)
                print("Item deleted successfully!")
            except ValueError:
                print("Item not found in main menu.")

#Add item
def add_item():
    category = input("Enter category: ").strip().title()
    item_name = input("Enter item name: ").strip().title()
    while True:
        try:
            price = int(input("Enter price: ").strip())
            break
        except ValueError:
            print("Price must be a number.")

    add_menu_item({
        "category": category,
        "item": item_name,
        "price": price
    })

    print("Item added successfully!")


if __name__ == "__main__":
    view_menu(get_menu(), allow_edit=True)
    search_menu(get_menu())
