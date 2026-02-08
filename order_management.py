from menu_database import get_menu

# Dictionary to store orders by table or invoice (only the lastest order will be stored)
orders = {}

#ORDER MENU DISPLAY
def order_type(current_user):
    while True:
        print("\nSelect the order type:")
        print("1. Dine-in")
        print("2. Takeaway")
        print("3. Back to Order Menu")

        try:
            user_input = int(input("Choose between 1-3: "))
        except ValueError:
            print("Must be a number.")
            continue

        if user_input == 1:
            dine_in(current_user)
        elif user_input == 2:
            takeaway(current_user)
        elif user_input == 3:
            print("\nSession ended.")
            break
        else:
            print("Invalid option. Please choose 1-3.")

def dine_in(current_user):
    table_num = input("Insert table number: ")

    if table_num in orders:
        print("Existing order found:")
        show_orders(table_num)

    print(f"Dine-in selected. Table number: {table_num}")
    add_order("Dine-in", table_num, current_user)

def takeaway(current_user):
    invoice_num = input("Insert invoice number: ")
    if invoice_num in orders:
        print("Existing order found:")
        show_orders(invoice_num)
        
    print(f"Takeaway selected. Invoice number: {invoice_num}")
    add_order("Takeaway", invoice_num, current_user)

def add_order(order_type, extra_info, current_user):

    current_menu = get_menu()
    current_order = []

    while True:
        print("=== MENU ===")
        column_width = "{:<5} | {:<20} | {:<55} | {:<10}"
        header = column_width.format("No.", "Category", "Item" , "Price")
        print(header)
        print("-" * len(header))

        for i, item in enumerate(current_menu, start=1):
            price_format = f"Rp{item['price']:,}".replace(",",".")
            print(column_width.format(i, item["category"], item["item"], price_format))
        
        if current_order:
            print("\nCurrent Order:")
            for i, order in enumerate(current_order, start=1):
                print(f"{i}. {order['quantity']} x {order['item']} = Rp{order['total']:,}".replace(",", "."))

        #Input item number
        try:
            user_input = int(input("\nSelect item number (type '0' to finish): "))
        except ValueError:
            print("Must be a number. Try again.")
            continue

        if user_input == 0:
            if not current_order:
                print("No items ordered")
            else:
                if order_type == "Dine-in":
                    print(f"Finish ordering. Table {extra_info}")
                else:
                    print(f"Finish ordering. Invoice {extra_info}")
                
                #show only current table/invoice order
                if extra_info in orders:
                    orders[extra_info]["items"].extend(current_order)
                    orders[extra_info]["cashier"] = current_user
                else:
                    orders[extra_info] = {
                        "cashier": current_user,
                        "items": current_order
                    }
                show_orders(extra_info)
            break 

        elif not (1 <= user_input <= len(current_menu)):
            print("Invalid input. Try again")
            continue

        #INPUT QUANTITY
        item = current_menu[user_input - 1]
        
        try:
            qty = int(input(f"Insert the quantity for {item['item']}: "))
            if qty <= 0:
                print("Quantity must be greater than 0. Try again.")
                continue
        except ValueError:
            print("Must be number. Try again.")
            continue
        
        #STORE THE ORDER ITEM
        order_item = {
            "order_type": order_type,
            "extra_info": extra_info,
            "category": item['category'],
            "item": item['item'],
            "price": item['price'],
            "quantity": qty,
            "total": item['price'] * qty
        }

        current_order.append(order_item)

def show_orders(extra_info):
    if extra_info not in orders or not orders[extra_info]:
        print(f"No orders yet for {extra_info}.")
        return

    order_data = orders[extra_info]
    current_order = order_data["items"]
    
    print(f"\nCashier: {order_data['cashier']}")

    print(f"=== ALL ORDER SUMMARY FOR {extra_info}===")
    column_width = "{:<5} | {:<30} | {:<10} | {:<15} | {:<15}"
    header = column_width.format("No.", "Item", "Qty", "Price", "Total")
    print(header)
    print("-" * len(header))

    grand_total = 0
    for idx, order in enumerate(current_order, start=1):
        price_format = f"Rp{order['price']:,}".replace(",", ".")
        total_format = f"Rp{order['total']:,}".replace(",", ".")
        print(column_width.format(idx, order['item'], order['quantity'], price_format, total_format))
        grand_total += order['total']

    grand_total_format = f"Rp{grand_total:,}".replace(",", ".")
    print(f"\nGrand Total: {grand_total_format}")

if __name__ == "__main__":
    order_type("TEST_USER")
