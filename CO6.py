alternatives = [
    {
        "name": "Laptop A",
        "price": 45000,
        "rating": 4.5,
        "probability": 0.8
    },

    {
        "name": "Laptop B",
        "price": 55000,
        "rating": 4.8,
        "probability": 0.9
    }
]

budget = 50000

best_choice = None
best_score = 0

for item in alternatives:

    # CSP Constraint
    if item["price"] > budget:
        print(item["name"], "Rejected due to budget")
        continue

    # Utility Score
    utility = item["rating"] * item["probability"]

    print(item["name"], "Utility:", utility)

    if utility > best_score:
        best_score = utility
        best_choice = item["name"]

print("\nFinal Recommendation:", best_choice)