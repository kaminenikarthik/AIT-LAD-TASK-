def is_safe(graph, colors, vertex, color):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, colors, vertex, num_colors):
    if vertex == len(graph):
        return True
    for color in range(1, num_colors + 1):
        if is_safe(graph, colors, vertex, color):
            colors[vertex] = color
            if graph_coloring(graph, colors, vertex + 1, num_colors):
                return True
            colors[vertex] = 0
    return False

graph = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3],
    [1, 2]
]
num_colors = 3
colors = [0] * 4

if graph_coloring(graph, colors, 0, num_colors):
    zones = ["", "Zone 1", "Zone 2", "Zone 3"]
    groups = ["A", "B", "C", "D"]
    print("Valid Seating Arrangement:")

    for i in range(4):
        print("Group", groups[i], "->", zones[colors[i]])
else:
    print("No valid seating arrangement exists.")
