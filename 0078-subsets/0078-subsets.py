class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, subSets = [], []

        def helper(i, nums, curSet, subSet):
            if i >= len(nums):
                subSet.append(curSet.copy())
                return

            curSet.append(nums[i])
            helper(i + 1, nums, curSet, subSet)
            curSet.pop()

            helper(i + 1, nums, curSet, subSet)

        helper(0, nums, curSet, subSets)
        return subSets

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna