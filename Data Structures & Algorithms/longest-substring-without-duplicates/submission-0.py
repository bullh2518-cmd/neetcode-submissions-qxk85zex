from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        window_counter = Counter()
        for end, leading_char in enumerate(s):
            window_counter[leading_char] += 1

            while window_counter[leading_char] > 1:
                trailing_char = s[start]
                window_counter[trailing_char] -= 1
                start += 1
            longest = max(end - start + 1, longest)
        return longest


            