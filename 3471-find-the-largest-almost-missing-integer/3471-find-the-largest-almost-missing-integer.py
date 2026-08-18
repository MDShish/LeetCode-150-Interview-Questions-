class Solution:
    def largestInteger(self, A: List[int], k: int) -> int:
        f = [0] * 51
        for x in A:
            f[x] += 1

        res, n = -1, len(A)
        for i, c in enumerate(A):
            if k == n or (f[c]==1 and (k==1 or not i or i+1==n)):
                res = max(res, c)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna