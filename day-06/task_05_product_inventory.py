# Task-05 : Product Inventory

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 0
}

# Display inventory
print("Inventory:")

for product, quantity in inventory.items():
    print(product, ":", quantity)

# Search product
product = input("Enter product to search: ")

if product in inventory:
    print("Quantity:", inventory[product])
else:
    print("Product not found")

# Update quantity
update_product = input("Enter product to update: ")

if update_product in inventory:
    new_quantity = int(input("Enter new quantity: "))
    inventory[update_product] = new_quantity
    print("Quantity updated.")
else:
    print("Product not found")

# Check out-of-stock products
print("Out of stock products:")

for product, quantity in inventory.items():
    if quantity == 0:
        print(product)