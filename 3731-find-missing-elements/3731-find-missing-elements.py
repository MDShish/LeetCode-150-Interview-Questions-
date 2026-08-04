class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        for i in range(nums[0], nums[len(nums) - 1]):
            if i not in nums:
                res.append(i)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna