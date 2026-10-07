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

def dfs(graph, folder, visited):
    if folder not in visited:
        print(folder)
        visited.add(folder)

        for subfolder in graph[folder]:
            dfs(graph, subfolder, visited)

print("Folders and Subfolders (DFS):")
visited = set()
dfs(file_system, "Root", visited)
