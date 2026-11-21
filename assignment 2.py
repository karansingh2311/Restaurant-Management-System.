#Resturant management system
name = input("Enter customer name: ")

total = 0

# Menu
menu = {
    1: ["Pizza", 250],
    2: ["Burger", 120],
    3: ["Pasta", 180],
    4: ["Momos", 100],
    5: ["Cold Drink", 50]
}

print("\n----- MENU -----")

for key, value in menu.items():
    print(key, value[0], "Rs.", value[1])

# Taking order

items = []

for i in range(1, 4):

    choice = int(input("\nEnter item number (0 to stop): "))

    if choice == 0:
        break

    if choice in menu:

        quantity = int(input("Enter quantity: "))

        item_name = menu[choice][0]
        price = menu[choice][1]

        amount = price * quantity
        total = total + amount

        items.append([item_name, quantity, amount])

    else:
        print("Invalid item number!")


# Discount

if total > 1000:
    discount = total * 0.10
elif total > 500:
    discount = total * 0.05
else:
    discount = 0


# Final bill

final_amount = total - discount

print("\n===== BILL =====")
print("Customer Name:", name)

for item in items:
    print(item[0], "x", item[1], "=", "Rs.", item[2])

print("----------------------")
print("Total Bill: Rs.", total)
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)

print("\nThank you for visiting!")