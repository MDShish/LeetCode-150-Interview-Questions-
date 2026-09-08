class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_val
            if temp > max_val:
                max_val = temp
        return arr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna