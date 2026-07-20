# class Solution:
#     def frequencySort(self, nums: List[int]) -> List[int]:
#         freq = {}
#         for n in nums:
#             freq[n] = freq.get(n, 0) + 1

#         arr = []

#         for num in sorted(freq):
#             arr.extend([num] * freq[num])

#         return arr


from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        nums.sort(key=lambda x: (freq[x], -x))
        return nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna