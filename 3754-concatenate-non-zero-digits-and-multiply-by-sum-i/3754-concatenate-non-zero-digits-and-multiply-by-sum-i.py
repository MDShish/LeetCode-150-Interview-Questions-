# class Solution:
#     def sumAndMultiply(self, n: int) -> int:
#         digit_sum = 0
#         t = str(n)
#         l1 = []
#         for e in t:
#             if e != "0":
#                 l1.append(e)
#         if not l1:
#             return 0
#         for w in l1:
#             digit_sum += int(w)
#         res = int("".join(l1)) * digit_sum
#         return res

# =============================================================

# class Solution:
#     def sumAndMultiply(self, n: int) -> int:
#         digits = []
#         digit_sum = 0

#         for ch in str(n):
#             if ch != '0':
#                 digits.append(ch)
#                 digit_sum += int(ch)

#         if not digits:
#             return 0

#         number = int("".join(digits))
#         return number * digit_sum

# ======================================

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [d for d in str(n) if d != '0']

        if not digits:
            return 0

        number = int("".join(digits))
        digit_sum = sum(int(d) for d in digits)

        return number * digit_sum
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna