def add_item(inventory, name, price, quantity):
    """
    Add a new item to the inventory.
    
    Args:
    inventory (dict): The current inventory
    name (str): The name of the item
    price (str): The price of the item
    quantity (str): The quantity of the item
    """
    # 3. When adding a new item with the same name as an existing one, the system overwrites the old item without any warning. We've lost data because of this. It would be helpful to have a confirmation prompt before overwriting.
    # Check if item already exists in the inventory
    if name in inventory:
        print(f"Warning: Overwriting existing item '{name}'.")
        # Ask user if they want to proceed
        proceed = input("Do you want to proceed? (Y/N): ")
        if proceed.lower()!= "y":
            return

    # Add the new item to the inventory
    inventory[name] = {"price": price, "quantity": quantity}
    print(f"{name} added to the inventory.")

def remove_item(inventory, item_name):
    """
    Remove an item from the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to remove
    """
    del inventory[item_name]
    print(f"{item_name} removed from the inventory.")

def update_quantity(inventory, item_name, new_quantity):
    """
    Update the quantity of an item in the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to update
    new_quantity (str): The new quantity of the item
    """
    # Check if the item is already in the inventory or not
    if item_name not in inventory:
        print(f"{item_name} is not in the inventory.")
        return

    # Check if the new quantity is a positive integer
    elif not new_quantity.isdigit() or int(new_quantity) < 0:
        print("Invalid quantity. Please enter a positive integer.")
        return
    # Update the quantity of an item in the inventory using item name (given that conditions are met)
    else:
        inventory[item_name]["quantity"] = new_quantity
        print(f"Quantity of {item_name} updated to {new_quantity}.")
        display_inventory(inventory)
    
def display_inventory(inventory):
    """
    Display all items in the inventory.
    
    Args:
    inventory (dict): The current inventory
    """
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for name in inventory:
            item = inventory[name]
            print(f"{name}: Price: ${item['price']:.2f}, Quantity: {item['quantity']}")

# Initialize inventory with two example items
inventory = {
    "apple": {"price": 0.50, "quantity": 100},
    "banana": {"price": 0.75, "quantity": 150}
}

while True:
    print("\n1. Add item\n2. Remove item\n3. Update quantity\n4. Display inventory\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter item name: ")
        price = input("Enter item price: ")
        quantity = int(input("Enter item quantity: "))
        add_item(inventory, name, price, quantity)
    elif choice == "2":
        name = input("Enter item name to remove: ")
        remove_item(inventory, name)

    elif choice == "3":
        name = input("Enter item name to update: ")
        quantity = input("Enter new quantity: ")

        update_quantity(inventory, name, quantity)
    elif choice == "4":
        display_inventory(inventory)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

