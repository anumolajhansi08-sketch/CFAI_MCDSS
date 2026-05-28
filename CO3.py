laptops = [
    {"name": "Laptop A", "price": 45000, "rating": 4.5},
    {"name": "Laptop B", "price": 60000, "rating": 4.8},
    {"name": "Laptop C", "price": 40000, "rating": 4.2}
]

budget = 50000
minimum_rating = 4.3

valid_options = []

for laptop in laptops:

    if laptop["price"] > budget:
        print(f"{laptop['name']} rejected because price exceeds budget")
        continue

    if laptop["rating"] < minimum_rating:
        print(f"{laptop['name']} rejected because rating is low")
        continue

    valid_options.append(laptop)

print("\nValid Alternatives:")

for item in valid_options:
    print(item["name"])