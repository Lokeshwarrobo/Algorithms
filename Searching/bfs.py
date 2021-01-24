queue = []
visited = []

def bfs(graph, node):
    queue.append(node)
    visited.append(node)
    while len(queue) != 0:
        cur = queue.pop(0)
        print(cur, end = ' ')

        for obj in graph[cur]:
            if obj not in visited:
                queue.append(obj)
                visited.append(obj)

bfs(graph, node)
