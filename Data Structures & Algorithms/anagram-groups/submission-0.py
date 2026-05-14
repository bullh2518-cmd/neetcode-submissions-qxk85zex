class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = set()

        for i in range(len(strs)):
            group = []

            for j in range(len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])

            hashset.add(tuple(sorted(group)))

        answer = []

        for group in hashset:
            answer.append(list(group))

        return answer