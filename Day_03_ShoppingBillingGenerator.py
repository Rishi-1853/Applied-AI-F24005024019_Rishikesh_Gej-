print("===== SHOPPING BILL GENERATOR =====")

total_bill = 0
items = []

n = int(input("Enter the number of items: "))

for i in range(n):
    print(f"\nItem {i+1}")
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    amount = quantity * price
    total_bill += amount

    items.append([item_name, quantity, price, amount])

print("\n========== BILL ==========")
print("{:<15} {:<10} {:<10} {:<10}".format(
    "Item", "Quantity", "Price", "Amount"))

for item in items:
    print("{:<15} {:<10} {:<10.2f} {:<10.2f}".format(
        item[0], item[1], item[2], item[3]))

print("-------------------------------")
print(f"Total Bill Amount: ₹{total_bill:.2f}")
print("===============================")

discount = 0
if total_bill > 5000:
    discount = total_bill * 0.10  # 10% discount

final_amount = total_bill - discount

print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")

print("\nThank you for shopping!")