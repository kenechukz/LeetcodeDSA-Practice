class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        """
        R:
        inp: s - str
         min <= sub size <= maxSize
         maxLetters -  max no. distinct letters (26)
        return max number of occurences

        E:
        if len s < minSize:
            return 0 
        
        A:
        maxLetters = 2, minSize = 3, maxSize = 4
        s = "aababcaab"
               ^ 
            l to r till =min size reached
            add to map (tmp chang on each loop)
            two for loops
            each iter cnt -  distinct letters
            if cnt > maxLtrs:

            add new letter tro cur sub while < maxSize

            aab
            aba
            bab
            keep track of maxOccurence

        s = "aaba"
         aab
         aba
         aaba
        O(n^2)
          

        map - sub: count 

        aababcaab
        l r
        inc r while < minSize
        
        """

        maxOcc = 0
        occ = dict()
        n = len(s)

        if n < minSize:
            return 0

        # Find all sub strings
        for i in range(n):
            for j in range(i + minSize-1, min(i + maxSize, n)):
                curSub = s[i:j +1]
                if len(set(curSub)) <= maxLetters: 
                    occ[curSub] = occ.get(curSub, 0) + 1
                    maxOcc = max(maxOcc, occ[curSub])

        return maxOcc
                
                
                




        