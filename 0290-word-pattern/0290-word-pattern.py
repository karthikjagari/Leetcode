class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ctw = {}
        wtc = {}
        words = s.split()
        if len(pattern) != len(words):
         return False

        ans = True
    
        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]
            if ch not in ctw and word not in wtc:
                ctw[ch] = word
                wtc[word] = ch
            elif ch in ctw and ctw[ch]!= word:
                ans = False
                break
            elif word in wtc and wtc[word]!=ch:
                ans =False
                break
        return ans
        
