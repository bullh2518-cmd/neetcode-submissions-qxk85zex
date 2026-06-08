from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        window_count = Counter()

        have = 0
        need = len(t_count)

        res = [-1, -1]
        resLen = float("infinity")

        l = 0

        if len(t) > len(s):
            return ""

        for r in range(len(s)):
            c = s[r]
            window_count[c] += 1

            if c in t_count and window_count[c] == t_count[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window_count[s[l]] -= 1

                if (
                    s[l] in t_count
                    and window_count[s[l]] < t_count[s[l]]
                ):
                    have -= 1

                l += 1

        l, r = res

        return s[l:r + 1] if resLen != float("infinity") else ""

