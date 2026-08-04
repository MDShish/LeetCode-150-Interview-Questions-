class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(min(nums), max(nums)):
            if i not in nums:
                res.append(i)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna