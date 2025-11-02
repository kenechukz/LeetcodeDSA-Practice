class Solution:
    def partitionString(self, s: str) -> List[str]:

        """
        R:
        given string: s

        partition it into unique segments like so:

        if seg not seen before add to seen segments
        else extend it until it hasn't beenm seen

        E:
        1 <= s.length <= 10^5
        s contains only lowercase English letters.

        A:
        c = cur seg to check
        "abbccccd"
         c
         j
        """

        seen = set()
        res = []
        cur = 0
        j = 0

        while j < len(s):
            seg = s[cur:j+1]
            if not seg in seen:
                seen.add(seg)
                res.append(seg)
                j+=1
                cur=j
            else:
                j+=1

        return res
            


        