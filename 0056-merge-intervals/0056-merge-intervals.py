class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        R:
        intervals - non sorted

        return array of non-overlap intervals
        constraints: 1 <= len(intrvals) <= 10^4

        E:
        if len(intervals) == 1:
            return intervals

        A:
        [[1,3],[2,9],[8,10],[15,18]]
        iter: i <- 1 to n
        prev [1,3]
        cur [2,9]
        [[1,3],[2,9],[8,12],[11,18]]
        if cur[0] < prev[1]
            merge
            cur = [min(start), max(end)]
        [[1,18]]

        """
        n = len(intervals)
        res = []
        if n == 1:
            return intervals
        intervals.sort()
        prev = intervals[0]
        for i in range(1,n):
            cur = intervals[i]
            if cur[0] <= prev[1]:
                cur = [prev[0], max(prev[1],cur[1])]
            else:
                res.append(prev)
            prev = cur
        res.append(prev)

        return res
        