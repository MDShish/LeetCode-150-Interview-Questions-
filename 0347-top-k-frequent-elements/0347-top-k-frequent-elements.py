# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hsh = Counter(nums)
#         # Sort items by frequency in descending order and extract keys
#         most_common = sorted(hsh.items(), key=lambda x: x[1], reverse=True)
#         result = [item[0] for item in most_common[:k]]
#         return result
    

#     ==============================================================================

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = Counter(nums)
        # Sort items by frequency in descending order and extract keys
        most_common = sorted(hsh, key=hsh.get, reverse=True)
        result = most_common[:k]
        return result
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna