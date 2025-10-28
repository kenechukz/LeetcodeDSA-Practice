class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        R:


        return array of non-overlapping intervals

        E:
        is input sorted ? NO
        if len(intervals) == 1:
            return intervals

        A:
        non overlapping if cur.start >= prev.end:
        [1,3] [3, 5]


        res = [[1, 3], [3, 5]]

        [[1,3],[2,6],[8,20],[9,18]]    

        res = [[1,6], [8, 20]]
        """

            
        res = []
        intervals.sort()

        for it in intervals:
            start = it[0]
            end = it[1]
            if not res:
                res.append(it)
            elif start <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], end)]
                
            else:
                res.append(it)

        return res





        return res
        