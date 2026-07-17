class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def helper2(i, curComb, n, k):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            if i > n:
                return

            for j in range(i, n + 1):
                curComb.append(j)
                helper2(j + 1, curComb, n, k)
                curComb.pop()

        helper2(1, [], n, k)
        return combs

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna