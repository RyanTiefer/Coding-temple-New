item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = 0.075   # 7.5% sales tax

# Variables for output
qty_1 = int(item1_qty)
qty_2 = int(item2_qty)
qty_3 = int(item3_qty)

price_1 = float(item1_price) * qty_1
price_2 = float(item2_price) * qty_2
price_3 = float(item3_price) * qty_3

tax = float(tax_rate)
subtotal = price_1 + price_2 + price_3
total = subtotal + (subtotal * tax)

print("=" * 60)
print("STORE RECEIPT")
print("=" * 60)

print(f"{item1_name} ${float(item1_price):.2f} x {item1_qty} = ${price_1:.2f}")
print(f"{item2_name} ${float(item2_price):.2f} x {item2_qty} = ${price_2:.2f}")
print(f"{item3_name} ${float(item3_price):.2f} x {item3_qty} = ${price_3:.2f}")

print("-" * 60)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7.5%): ${(subtotal * tax):.2f}")

print("=" * 60 )
print(f"Total: ${total:.2f}")
print("=" * 60 )