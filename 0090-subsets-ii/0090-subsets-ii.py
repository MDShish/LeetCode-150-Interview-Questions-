class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curSet, subSets = [], []

        def helper(i, nums, curSet, subSet):
            nums.sort()
            if i >= len(nums):
                subSet.append(curSet.copy())
                return

            curSet.append(nums[i])
            helper(i + 1, nums, curSet, subSet)
            curSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, nums, curSet, subSet)

        helper(0, nums, curSet, subSets)
        return subSets

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna