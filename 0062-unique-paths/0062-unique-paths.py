class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        """
        R:
        Given m rows and n columns
        return no. of ways to reach grid[m-1][n-1] 

        E:

        |R|
        if grid[0][0] == grid[m-1][n-1]

        if row == m-1:
            only move right



        |R | |
        m = 1, n = 2
        need to validate move down and move right are on grid

        at each step we have a choice, move down or move right


        Recursive Rule:
        we start with 1 x 1, then expand by 1 each time
        1 x 1 = 0
        2 x 2 = 2
        3 x 3 = 
        """

        prevRow = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + prevRow[j]

            prevRow = newRow

        return prevRow[0]

        




        







        