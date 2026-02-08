#Initial menu data
menu_list = [
    {"category": "Appetizers", "item": "Spring Rolls", "price": 30000},
    {"category": "Appetizers", "item": "Garlic Bread", "price": 25000},
    {"category": "Appetizers", "item": "Chicken Wings", "price": 40000},

    {"category": "Main Courses", "item": "Grilled Chicken with Rice", "price": 65000},
    {"category": "Main Courses", "item": "Beef Steak", "price": 120000},
    {"category": "Main Courses", "item": "Fried Rice", "price": 45000},
    
    {"category": "Drinks", "item": "Mineral Water", "price": 10000},
    {"category": "Drinks", "item": "Iced Tea", "price": 15000},
    {"category": "Drinks", "item": "Coffee", "price": 20000},

    {"category": "Desserts", "item": "Ice Cream", "price": 20000},
    {"category": "Desserts", "item": "Chocolate Cake", "price": 30000},
    {"category": "Desserts", "item": "Vanilla Panna Cotta", "price": 40000},
]
#Return the lastest menu
def get_menu():
    return menu_list.copy()

#Add a new item to the menu
def add_menu_item(item_dict):
    if "category" in item_dict and \
       "item" in item_dict and \
       "price" in item_dict:
        menu_list.append(item_dict)