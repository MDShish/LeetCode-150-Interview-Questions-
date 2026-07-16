class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            count = 1
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                x, y = q.popleft()

                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    nr, nc = x + dr, y + dc

                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        count += 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea



# ====================================


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited):
                visited.add((r, c))
                return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

            return 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna