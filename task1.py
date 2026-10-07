from collections import deque

# File system represented as a graph
file_system = {
    "Root": ["Documents", "Downloads", "Pictures"],
    "Documents": ["Projects", "Notes"],
    "Downloads": ["Software"],
    "Pictures": ["Photos", "Wallpapers"],
    "Projects": [],
    "Notes": [],
    "Software": [],
    "Photos": [],
    "Wallpapers": []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("Folders Level by Level (BFS):")

    while queue:
        folder = queue.popleft()

        if folder not in visited:
            print(folder)
            visited.add(folder)

            for subfolder in graph[folder]:
                if subfolder not in visited:
                    queue.append(subfolder)

bfs(file_system, "Root")
