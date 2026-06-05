from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_size = len(s1)

        s1_count = Counter(s1)
        window_count = Counter(s2[:window_size])

        if window_count == s1_count:
            return True

        for r in range(window_size, len(s2)):
            new_char = s2[r]
            old_char = s2[r - window_size]

            window_count[new_char] += 1
            window_count[old_char] -= 1

            if window_count[old_char] == 0:
                del window_count[old_char]

            if window_count == s1_count:
                return True

        return False

            
        
        

