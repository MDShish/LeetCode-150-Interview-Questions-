class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # cols = collections.defaultdict(set)
        # rows = collections.defaultdict(set)
        # squares = collections.defaultdict(set)  # key = (r//3, c//3)
        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue
        #         if (board[r][c] in rows[r] or 
        #             board[r][c] in cols[c] or 
        #             board[r][c] in squares[(r//3, c//3)]):
        #             return False
        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r//3, c//3)].add(board[r][c])
        # return True
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if (i, val) in seen or (val, j) in seen or (i//3, j//3, val) in seen:
                    return False
                seen.add((i, val))
                seen.add((val, j))
                seen.add((i//3, j//3, val))
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna