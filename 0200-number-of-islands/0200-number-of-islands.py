# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         islands = 0
#         visited = set()
#         rows, cols = len(grid), len(grid[0])

#         def bfs(r, c):
#             q = deque()
#             visited.add((r, c))
#             q.append((r, c))

#             while q:

#                 x, y = q.popleft()
#                 directions = [[1,0],[-1,0],[0,1],[0,-1]]

#                 for dr, dc in directions:
#                     a, b = x + dr, y + dc
#                     if 0 <= a < rows and 0 <= b < cols and grid[a][b] == "1" and (a, b) not in visited:
#                         visited.add((a, b))
#                         q.append((a, b))
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visited:
#                     islands += 1
#                     bfs(r, c)
#         return islands


# ======================================================================================================================================================





class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited):
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna