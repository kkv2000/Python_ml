order = {}
for _ in range(int(input("Enter the limit : "))):
    item, space, price = input("Enter the name and price : ").rpartition(' ')
    order[item] = order.get(item, 0) + int(price)
print("TOTAL ITEMS")
for item, price in order.items():
    print(item, price)
