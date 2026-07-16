class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        queue = collections.deque([(0, 0, 1)]) # (row, col, distance)
        grid[0][0] = 1 # Mark as visited

        while queue:
            r, c, d = queue.popleft()
            if r == n - 1 and c == n - 1:
                return d
            
            # Explore all **8 neighbors**
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0: continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc, d + 1))
        return -1



# ==========================================================

# dfs solution - not optimal, Just for learning purpose

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        ans = float("inf")
        visited = set()

        def dfs(r, c, dist):
            nonlocal ans

            if (r < 0 or c < 0 or
                r >= n or c >= n or
                grid[r][c] == 1 or
                (r, c) in visited):
                return

            if dist >= ans:
                return

            if r == n - 1 and c == n - 1:
                ans = min(ans, dist)
                return

            visited.add((r, c))

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    dfs(r + dr, c + dc, dist + 1)

            visited.remove((r, c))   # Backtrack

        dfs(0, 0, 1)

        return ans if ans != float("inf") else -1




# ==========================================================

# bfs inside function.





from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        def bfs(r, c):
            q = deque()
            q.append((r, c, 1))   # row, col, distance
            grid[r][c] = 1        # mark visited

            while q:
                x, y, dist = q.popleft()

                if x == n - 1 and y == n - 1:
                    return dist

                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == 0 and dc == 0:
                            continue

                        nr, nc = x + dr, y + dc

                        if (0 <= nr < n and
                            0 <= nc < n and
                            grid[nr][nc] == 0):

                            grid[nr][nc] = 1
                            q.append((nr, nc, dist + 1))

            return -1

        return bfs(0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna