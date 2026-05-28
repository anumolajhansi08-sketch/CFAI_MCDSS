tree = {
    "A": ["B", "C"],
    "B": [3, 5],
    "C": [2, 9]
}

def minimax(node, maximizing):

    if isinstance(node, int):
        return node

    children = tree[node]

    if maximizing:
        return max(minimax(child, False) for child in children)

    else:
        return min(minimax(child, True) for child in children)

result = minimax("A", True)

print("Best Utility Value:", result)