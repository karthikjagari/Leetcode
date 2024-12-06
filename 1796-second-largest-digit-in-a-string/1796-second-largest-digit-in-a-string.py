class Solution:
    def secondHighest(self, s: str) -> int:
        max1 = -1
        max2 = -1
        for char in s:
            if char.isnumeric():
                if int(char) > max1:
                    max2 = max1
                    max1 = int(char)
                elif int(char) >max2 and int(char) <max1:
                    max2=int(char)
            
        return max2



        