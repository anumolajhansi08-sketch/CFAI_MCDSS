from dataclasses import dataclass
from typing import Dict, List
import heapq

# ---------- Dataclass ----------
@dataclass
class Alternative:
    name: str
    criteria: Dict[str, float]

# ---------- Criteria Weights ----------
weights = {
    "cost": 0.3,
    "quality": 0.4,
    "performance": 0.2,
    "preference": 0.1
}

# ---------- Alternatives ----------
alternatives = [
    Alternative("Laptop A", {
        "cost": 8,
        "quality": 9,
        "performance": 8,
        "preference": 7
    }),

    Alternative("Laptop B", {
        "cost": 7,
        "quality": 8,
        "performance": 9,
        "preference": 8
    }),

    Alternative("Laptop C", {
        "cost": 9,
        "quality": 7,
        "performance": 7,
        "preference": 9
    })
]

# ---------- Utility Function ----------
def calculate_utility(option: Alternative) -> float:
    score = 0

    for key, value in option.criteria.items():
        score += value * weights[key]

    return score

# ---------- Ranking ----------
priority_queue = []

for item in alternatives:
    utility = calculate_utility(item)

    print(f"{item.name} Utility Score = {utility}")

    heapq.heappush(priority_queue, (-utility, item.name))

print("\nBest Recommendation:")

best = heapq.heappop(priority_queue)
print(best[1])