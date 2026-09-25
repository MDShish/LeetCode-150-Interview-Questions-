class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = "".join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(v) - 1
        while l < r:
            if v[l] != v[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna