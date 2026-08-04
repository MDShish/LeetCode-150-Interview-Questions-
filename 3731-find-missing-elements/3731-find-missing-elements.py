class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(min(nums), max(nums)):
            if i not in nums:
                res.append(i)
        return res



class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return (K:=set(nums)) and [x for x in range(min(K)+1, max(K)) if x not in K]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna