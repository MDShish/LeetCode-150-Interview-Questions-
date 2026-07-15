class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        old_color = image[sr][sc]
        if old_color == color:
            return image
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return
            if image[r][c] != old_color:
                return
            
            image[r][c] = color
            
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        dfs(sr, sc)
        return image

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna