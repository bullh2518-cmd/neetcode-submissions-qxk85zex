class Solution:

    def encode(self, strs: list[str]) -> str:
        Encode = ""

        for word in strs:
            Encode = Encode + str(len(word)) + "#" + word

        return Encode

    def decode(self, s: str) -> list[str]:
        Decode = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length

            word = s[word_start:word_end]

            Decode.append(word)

            i = word_end

        return Decode
