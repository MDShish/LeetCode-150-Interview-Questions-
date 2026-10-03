class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        st = [-1]
        
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                st.pop()
                
                if not st:
                    st.append(i)
                else:
                    res = max(res, i - st[-1])
                    
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna