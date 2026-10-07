import heapq

def a_star(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    cost_so_far = {start: 0}
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal:
            return path, g
        for neighbor, cost in graph[current]:
            new_cost = g + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                # f(n) = g(n) + h(n)
                f_cost = new_cost + heuristic[neighbor]

                heapq.heappush(
                    pq,
                    (f_cost, new_cost, neighbor, path + [neighbor])
                )
    return None, float("inf")

graph = {
    'Accident': [('A', 4), ('B', 2)],
    'A': [('C', 5), ('D', 10)],
    'B': [('A', 1), ('D', 6)],
    'C': [('Hospital', 3)],
    'D': [('Hospital', 2)],
    'Hospital': []
}
heuristic = {
    'Accident': 7,
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 2,
    'Hospital': 0
}
start = 'Accident'
goal = 'Hospital'
path, cost = a_star(graph, heuristic, start, goal)
if path:
    print("Fastest Path:", " -> ".join(path))
    print("Total Travel Cost:", cost)
else:
    print("No path to the hospital.")
