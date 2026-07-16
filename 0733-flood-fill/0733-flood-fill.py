# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         R, C = len(image), len(image[0])
#         old_color = image[sr][sc]
#         if old_color == color:
#             return image
#         def dfs(r, c):
#             if r < 0 or r >= R or c < 0 or c >= C:
#                 return
#             if image[r][c] != old_color:
#                 return
            
#             image[r][c] = color

#             dfs(r - 1, c)
#             dfs(r + 1, c)
#             dfs(r, c - 1)
#             dfs(r, c + 1)
#         dfs(sr, sc)
#         return image


# ================================================================================


# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         R, C = len(image), len(image[0])
#         old_color = image[sr][sc]

#         if old_color == color:
#             return image

#         def dfs(r, c):
#             if image[r][c] != old_color:
#                 return

#             image[r][c] = color

#             if r >= 1:
#                 dfs(r - 1, c)
#             if r + 1 < R:
#                 dfs(r + 1, c)
#             if c >= 1:
#                 dfs(r, c - 1)
#             if c + 1 < C:
#                 dfs(r, c + 1)

#         dfs(sr, sc)
#         return image


# ================================================================================


# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         R, C = len(image), len(image[0])
#         old_color = image[sr][sc]

#         if old_color == color:
#             return image

#         def dfs(r, c):
#             if image[r][c] == old_color:
#                 image[r][c] = color

#                 if r >= 1:
#                     dfs(r - 1, c)
#                 if r + 1 < R:
#                     dfs(r + 1, c)
#                 if c >= 1:
#                     dfs(r, c - 1)
#                 if c + 1 < C:
#                     dfs(r, c + 1)

#         dfs(sr, sc)
#         return image



# ================================================================================


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m: int = len(image)
        n: int = len(image[0])
        q: deque[tuple[int,int]] = deque()

        original_color: int = image[sr][sc]

        if original_color == color:
            return image

        visited: list[list[int]] = [[False]*n for _ in range(0, m)]

        # color first pixel
        image[sr][sc] = color
        visited[sr][sc] = True
        q.append((sr, sc))

        while len(q) != 0:
            size: int = len(q)

            for _ in range(0, size):
                x, y = q.popleft()
                # now put adj elements with original color

                # 4 dirs
                # 1. up
                if self.is_valid(x-1, y, image) and visited[x-1][y] is False and image[x-1][y] == original_color:
                    image[x-1][y] = color
                    q.append((x-1, y))
                    visited[x-1][y] = True

                # 1. down
                if self.is_valid(x+1, y, image) and visited[x+1][y] is False and image[x+1][y] == original_color:
                    image[x+1][y] = color
                    q.append((x+1, y))
                    visited[x+1][y] = True

                # 1. left
                if self.is_valid(x, y-1, image) and visited[x][y-1] is False and image[x][y-1] == original_color:
                    image[x][y-1] = color
                    q.append((x, y-1))
                    visited[x][y-1] = True

                # 1. right
                if self.is_valid(x, y+1, image) and visited[x][y+1] is False and image[x][y+1] == original_color:
                    image[x][y+1] = color
                    q.append((x, y+1))
                    visited[x][y+1] = True

        return image

    def is_valid(self, x: int, y: int, image: list[list[int]]) -> bool:
        if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
            return False

        return True 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna