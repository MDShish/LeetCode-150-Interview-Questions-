class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        n = len(candidates)
        def helper2(i, curComb):
            if sum(curComb) == target:
                combs.append(curComb.copy())
                return
            if i >= n or sum(curComb) > target:
                return

            for j in range(i, n):
                curComb.append(candidates[j])
                helper2(j, curComb)
                curComb.pop()

        helper2(0, [])
        return combs

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna