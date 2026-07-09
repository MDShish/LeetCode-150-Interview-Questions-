class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(u.lower() for u in s if u.isalnum())
        l,r = 0,len(filtered)-1
        while(l<r):
            if(filtered[l]!=filtered[r]):
                return False
            l, r = l+1, r-1
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna