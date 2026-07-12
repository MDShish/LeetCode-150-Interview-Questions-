# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = collections.defaultdict(list)
#         for s in strs:
#             count = [0]*26
#             for letter in s:
#                 count[ord(letter)- ord('a')]+=1
#             d[tuple(count)].append(s)
#         return list(d.values())



# ====================================================

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            mp[key].append(s)
        return list(mp.values())

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna