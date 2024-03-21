from collections import Counter

# Total shoes available in the shop
stock = int(input())

# List of shoe sizes available
sizes = [int(i) for i in input().split()]

# Number of customers
customers = int(input())


# Customer Orders
orders = [input().split() for _ in range(customers)]

# Create a size dictionary
sizes_dict = Counter(sizes)

# Initiate earnings
earnings = 0

# Calculate total earnings by looping through the customer orders
for order in orders:
    shoe_size = int(order[0])
    shoe_price = int(order[1])

    if shoe_size in sizes_dict:
        if sizes_dict[shoe_size] > 0:
            earnings += shoe_price
            sizes_dict[shoe_size] -= 1

print(earnings)
