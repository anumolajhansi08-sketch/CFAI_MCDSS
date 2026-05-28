from queue import Queue
import heapq

graph = {
    "Laptop A": ["Laptop B", "Laptop C"],
    "Laptop B": ["Laptop D"],
    "Laptop C": ["Laptop D"],
    "Laptop D": []
}

heuristic = {
    "Laptop A": 6,
    "Laptop B": 4,
    "Laptop C": 3,
    "Laptop D": 0
}

# ---------- BFS ----------
def bfs(start):
    visited = set()
    q = Queue()

    q.put(start)
    visited.add(start)

    print("BFS Traversal:")

    while not q.empty():
        node = q.get()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)

bfs("Laptop A")


# ---------- A* Search ----------
def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))

    g_cost = {start: 0}

    while open_set:
        current = heapq.heappop(open_set)[1]

        print("Evaluating:", current)

        if current == goal:
            print("Goal Found")
            return

        for neighbor in graph[current]:

            temp_cost = g_cost[current] + 1

            if neighbor not in g_cost or temp_cost < g_cost[neighbor]:

                g_cost[neighbor] = temp_cost

                f_cost = temp_cost + heuristic[neighbor]

                heapq.heappush(open_set, (f_cost, neighbor))

a_star("Laptop A", "Laptop D")