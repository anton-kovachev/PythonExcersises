import asyncio
from inventory import Inventory

TAX_RATE = 0.05;

def display_catalogue(catalogue):
    burgers = catalogue["Burgers"]
    sides = catalogue["Sides"]
    drinks = catalogue["Drinks"]

    print("--------- Burgers -----------\n")
    for burger in burgers:
        item_id = burger["id"]
        name = burger["name"]
        price = burger["price"]
        print(f"{item_id}. {name} ${price}")

    print("\n---------- Sides ------------")
    for side in sides:
        sizes = sides[side]

        print(f"\n{side}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n---------- Drinks ------------")
    for beverage in drinks:
        sizes = drinks[beverage]

        print(f"\n{beverage}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n------------------------------\n")


async def main():
    print("Welcome to the ProgrammingExpert Burger Bar!")
    print("Loading catalogue...")
    inventory = Inventory()
    display_catalogue(await inventory.get_catalogue())
    
    await make_order(inventory)

async def make_order(inventory):
    print("Please enter the number of items that you would like to add to your order. Enter q to complete your order.")
    order_input = None
    orders = []
    
    while order_input != "q":
        order_input = input("Enter an item number: ")
        if order_input == "q":
            pass
        elif not order_input.isdigit():
            print("Invalid order")
        elif inventory.items.get(int(order_input), None) == None:
            print("Ordered item does not exists")
        else:
            orders.append(int(order_input))
    
    print("Placing order...")
    removed_orders = await check_stock_availability(inventory, orders)
        
    for removed_order in removed_orders:
        print(f"Unfortunately item number {removed_order} is out of stock and has been removed from your order. Sorry!")
    
    total_price = await print_order(inventory, orders)
    confirm_input = input(f"Would you like to purchase this order for ${total_price} (yes/no)? ")
    
    if confirm_input == "yes":
        print("Thank you for your order!")
        new_order = input("Would you like to make another order (yes/no)? ")
        if new_order == "yes":
            await make_order(inventory)
        else:
            print("Goodbye")
    else:
        print("Goodbye")
    

async def print_order(inventory, orders):
    combos = await create_combos(inventory, orders)
    
    print("Here is a summary of your order:")
    subtotal_price = 0;
    
    for combo in combos:
        combo_price = 0

        for order in combo:
            orders.remove(order)
            combo_price += (await inventory.get_item(order))["price"]
            
        combo_price = combo_price * 0.85
        subtotal_price += combo_price
        print(f"${ round(combo_price, 2)} Burger Combo")
        
        for order in combo:
            await print_order_item(inventory, order, in_combo=True)

    for order in orders:
        item_price = await print_order_item(inventory, order)
        subtotal_price += item_price
    
    subtotal_price = round(subtotal_price, 2)
    print(f"Subtotal: ${subtotal_price}")
    
    tax = round(subtotal_price * TAX_RATE, 2)
    print(f"Tax: ${round(tax, 2)}")
    
    total_price = round(subtotal_price + tax, 2)
    print(f"Total: ${round(total_price, 2)}")
    
    return total_price

async def print_order_item(inventory, order, in_combo = False):
    item = await inventory.get_item(order)
    itemName = item['name'] if item.get('name', None) is not None else item['size'] + " " + item['subcategory']
    print(f" {"\t" if in_combo else ""} ${item['price'] if not in_combo else ""} {itemName}")
    return item['price']

async def check_stock_availability(inventory, orders):
    removed_orders = []
    
    for order in orders:
        if (await inventory.get_stock(order) < 1):
            removed_orders.append(order)
        else:
            await inventory.decrement_stock(order)
            
    for removed_order in removed_orders:
        orders.remove(removed_order)
    
    return removed_orders
    
async def create_combos(inventory, orders):
    orders = sorted(orders, key=lambda x: inventory.items[x]["price"], reverse=True)
    
    burgers = await filter_orders_by_category(inventory, orders, "Burgers")
    sides = await filter_orders_by_category(inventory, orders, "Sides")
    drinks = await filter_orders_by_category(inventory, orders, "Drinks")
    
    return zip(burgers, sides, drinks)
    
async def filter_orders_by_category(invetory, orders, category):
    category_orders = []
    
    for order in orders:
        if (await invetory.get_item(order))['category'] == category:
            category_orders.append(order)
    
    return category_orders

if __name__ == "__main__":
    asyncio.run(main())
