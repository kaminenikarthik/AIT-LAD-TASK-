import heapq

def a_star(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = set()
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return path, g
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )
    return None, float("inf")

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'G': []
}
heuristic = {
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 3,
    'E': 2,
    'G': 0
}
start = 'A'
goal = 'G'
path, cost = a_star(graph, heuristic, start, goal)
print("Shortest Route:")
print(" -> ".join(path))
print("Total Distance:", cost)
