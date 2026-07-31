class Solution:
    def minimumPushes(self, word: str) -> int:
        char_count = [0] * 26

        for ch in word:
            char_count[ord(ch) - ord('a')] += 1

        char_count.sort(reverse=True)

        min_push_count = 0

        for i in range(26):
            min_push_count += char_count[i] * (i // 8 + 1)

        return min_push_count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna