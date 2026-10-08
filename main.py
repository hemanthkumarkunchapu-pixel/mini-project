# Mini Project: Order Processing and Revenue Calculation

raw_orders = [
    {"item_name": "Pizza", "quantity": 2, "price": 10.99},
    {"item_name": "Burger", "quantity": 1, "price": 8.99},
    {"item_name": "Salad", "quantity": 3, "price": 6.99},
    {"item_name": "Pasta", "quantity": 1, "price": 12.99}
]

processed_orders = []

for order in raw_orders:
    name = " ".join(order["item_name"].split()).title()
    subtotal = order["quantity"] * order["price"]

    if subtotal >= 300:
        delivery_fee = 0
    else:
        delivery_fee = 30

    final_total = subtotal + delivery_fee

    processed_orders.append({
        "item_name": name,
        "quantity": order["quantity"],
        "total": final_total,
        "delivery_fee": delivery_fee
    })

print("Processed Orders:")
for o in processed_orders:
    print(o)

total_revenue = sum(order["total"] for order in processed_orders)
print(f"\nTotal Revenue: ${total_revenue:.2f}")
