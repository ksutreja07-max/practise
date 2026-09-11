product = "Laptop"
quantity = 2
price = 45000
customer_name = "Kuldip"

order = "Customer %s ordered %d %s at a price of %.2f each." % (customer_name, quantity, product, price)

print(order)

print("Uppercase:", order.upper())
print("Lowercase:", order.lower())

print("Position of Laptop:", order.find("Laptop"))

print("After replacement:", order.replace("Laptop", "Computer"))

print("Number of 'a':", order.count("a"))

print("Words:", order.split())