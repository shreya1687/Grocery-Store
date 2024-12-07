# List of items selected by the user
LIST_OF_ITEMS = []

def display_item():
    # dictionary to maintain list of items
    items_dict = {
        "pantry_essentials" : {
            "tea_leaves" : 100 ,
            "coffee" : 200,
            "aluminium_foil" : 100, 
            "sugar" : 60,    
        },
        "toileteries_cosmetics": {
            "toothpaste" : 110,
            "shampoo ": 300,
            "detergent_powder" : 250,
            "phenyl" : 299,
            "wiper" : 105,
            "incense_sticks" : 90,
        },
        "food_essentials" : {
            "macroni" : 100,
            "toor_dal" : 200,
            "urad_dal" : 100,
            "moong_dal" : 120,
            "basmati_rice" : 120,
        },
        "spices" : {
            "cumin_spice" : 99,
            "garam_masala" : 70,
        },
        "dry_fruits" : {
            "almonds" : 250,
            "cashew_nuts" : 300
        }        
    }
    
    return items_dict


def select_item():    
   
    # fetch list of items
    items_dict = display_item()
    # number of categories
    END_INDEX_CATEGORY = len(items_dict)
    # number of items in each category
    END_INDEX_ITEMS = 0
    
    print("Below is the list of item categories you wish to purchase ... ")
    for index, item in enumerate(items_dict.keys(), start=1):
        print(f"{index} ---> {item}")
    while True:
        category = input("Please select a category : ")
        if not category.isdigit():
            print("Invalid input.. Please select the correct category number from the list above.")
            continue
        if (1 > int(category)) or (int(category) > END_INDEX_CATEGORY):
            print("Invalid input.. Please select the correct category number within the range from the list above.")
            continue
        break
    print("Below is the list of items for the selected category ...")
    
    # display list of items for selected category
    for index, item in enumerate(items_dict.keys(), start=1):
        if index == int(category):
            for item_index, price in enumerate(items_dict[item].items(), start=1):
                print(item_index, end="---> ")
                for i in price:
                    print(i, end="  ")
                print()
            END_INDEX_ITEMS = len(items_dict[item])
    
    # Ask the user to select an item
    while True:
        select_items = input("Please select the item number you wish to add to cart: ").upper()        
        if not select_items.isdigit():
            print("Invalid input.. Please select the correct item number from the list above.")
            continue
        if (1 > int(select_items)) or (int(select_items) > END_INDEX_ITEMS):
            print("Invalid input.. Please select the correct item number within the range from the list above.")
            continue
        c = list(items_dict.keys())[int(category)-1]
        LIST_OF_ITEMS.append(list(items_dict[c].items())[int(select_items)-1])
        
        while True:
            ans = input("Do you wish to add more items (Y/N):").upper()
            if ans == "N":
                break
            elif ans == "Y":
                answ = input("Do you wish to add items from another category (Y/N):").upper()
                if answ == "N":
                    select_items = input("Please select the item number you wish to add to cart: ").upper()        
                    if not select_items.isdigit():
                        print("Invalid input.. Please select the correct item number from the list above.")
                        continue
                    if (1 > int(select_items)) or (int(select_items) > END_INDEX_ITEMS):
                        print("Invalid input.. Please select the correct item number within the range from the list above.")
                        continue
                    c = list(items_dict.keys())[int(category)-1]
                    LIST_OF_ITEMS.append(list(items_dict[c].items())[int(select_items)-1])
                elif answ == "Y":
                    select_item()
                    break
                else:
                    print("Invalid input...Try again!")
                    continue
            else:
                print("Invalid input.. Try again!")
                continue
            print("**************")
        break
        print("----------------")
    # Add all the selected items by the user to the cart
    return LIST_OF_ITEMS

def generate_invoice():
    total = 0
    lst_of_items = select_item()
    tuple_count = {}
    print("************************************")
    print("---------------Invoice--------------")
    for item in lst_of_items:
        if item in tuple_count:        
            tuple_count[item] +=1
        else:
            tuple_count[item] = 1
    
    for item, count in tuple_count.items():
        total += item[1]*count
        print(f" Item : {item[0]} | Unit Price: {item[1]} | Qty : {count} | Total Price : {item[1]*count}")
    
    print("--------TOTAL BILL--------", total)        
    
if __name__ == "__main__":
    
    print("Welome to Big Basket... Enjoy your time shopping !")
    
    # Select the items to buy
    # select_item()
    # Add to Cart
    # add_to_cart()
    # Calculate the total amount
    # calculate_total_of_items()
    #Ask user to enter the phone number and generate receipt
    generate_invoice()
    
    