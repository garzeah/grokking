class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj, visited, count = {}, set(), 0

        for i in range(n):
            adj[i] = []

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        # Using dfs to check each connected graph
        # then recording it in our adj_list
        for vertex in range(n):
            if vertex not in visited:
                self.dfs(vertex, edges, visited, adj)
                count += 1

        return count

    def dfs(self, vertex, edges, visited, adj):
        if vertex in visited:
            return

        # Recording each vertex we visit
        visited.add(vertex)

        for nei in adj[vertex]:
            self.dfs(nei, edges, visited, adj)

# Time complexity: O(V + E) because we are traversing
# each node once.

# Space Complexity: O(V + E) to build out the adjaceny list.

# Solution: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/400707/Simple-DFS-and-BFS-Python-solutions-using-a-dictionary