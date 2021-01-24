visited = []

def dfs(graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for obj in dfs[node]:
            dfs(graph, obj)
