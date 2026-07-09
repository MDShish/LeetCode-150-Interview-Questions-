# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}  # stores num: index

#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in hashmap:
#                 return [hashmap[complement], i]
#             hashmap[num] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # stores num: index

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna