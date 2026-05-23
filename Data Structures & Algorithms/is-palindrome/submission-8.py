class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        word = "".join(s)
        words = word.lower()

        for char in words:
            if char.isalnum():
                clean += char
                Left = 0
                Right = len(clean) - 1
            
        if clean == "":
            return True
        
        while Left < Right:
            if clean[Left] != clean[Right]:
                return False
            Left += 1
            Right -= 1

        return True