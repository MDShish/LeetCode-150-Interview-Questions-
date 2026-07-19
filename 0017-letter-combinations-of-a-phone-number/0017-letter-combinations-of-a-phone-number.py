class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToStr = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combs = []
        def helper(i, curLis):
            if len(curLis) == len(digits):
                combs.append("".join(curLis))
                return

            for ch in digitToStr[digits[i]]:
                curLis.append(ch)
                helper(i + 1, curLis)
                curLis.pop()

            
        helper(0, [])
        return combs

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna