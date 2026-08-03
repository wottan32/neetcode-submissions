class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[List[str]]:
        dicc = {} 

        for word in strs:
            sorted_word =''.join(sorted(word))
            if sorted_word not in dicc:
                dicc[sorted_word] = []
            dicc[sorted_word].append(word)
        return list(dicc.values())
