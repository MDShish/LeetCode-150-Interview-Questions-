class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        numtoRank = {}
        rank = 1
        sorted_arr = sorted(arr)
        for i in range(len(arr)):
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            numtoRank[sorted_arr[i]] = rank
        for i in range(len(arr)):
            arr[i] = numtoRank[arr[i]]
        return arr



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna