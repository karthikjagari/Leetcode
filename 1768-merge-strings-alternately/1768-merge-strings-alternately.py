class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1) , len(word2))

        results = []
        for i in range(min_len):
            results.append(word1[i])
            results.append(word2[i])
        results.append(word1[min_len : ])
        results.append(word2[min_len : ])
        return ''.join(results)



