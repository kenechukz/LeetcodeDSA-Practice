class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        """

        R:
        given mxn 2D grid, 
        1 - land
        0 - water

        return no. islands

        E:
        can we assume outside of grid is water? yes

        are m and n equal? no

        constraints?
        1 <= m, n <= 300

        A:
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]

        do dfs while changing 1 to 0

        O(m*n)
        O(m*n)

        when done incr no. islands count
        Output: 3
 
        """

        ROWS = len(grid)
        COLS = len(grid[0])


        islands=0

        def dfs(r,c):
            
            if min(r,c) < 0 or r > ROWS-1 or c > COLS-1 or grid[r][c] == "0":
                return 

            grid[r][c] = "0"
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r+1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands +=1
                    dfs(r,c)
        
        return islands