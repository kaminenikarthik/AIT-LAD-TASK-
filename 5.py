import random

time = [
    [0, 4, 7, 6],
    [4, 0, 3, 5],
    [7, 3, 0, 2],
    [6, 5, 2, 0]
]

n = 4
pheromone = [[1] * n for _ in range(n)]

best_route = None
best_time = float('inf')

for _ in range(100):
    route = [0]
    unvisited = set(range(1, n))

    while unvisited:
        current = route[-1]

        next_stop = min(
            unvisited,
            key=lambda x: time[current][x] / pheromone[current][x]
        )

        route.append(next_stop)
        unvisited.remove(next_stop)

    route.append(0)

    total = sum(time[route[i]][route[i+1]]
                for i in range(n))

    if total < best_time:
        best_time = total
        best_route = route

print("Best Route:", " -> ".join(map(str, best_route)))
print("Minimum Travel Time:", best_time, "minutes")
