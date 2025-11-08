class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        R:
        given m x n board
        with 'X's and 'O's

        capture surrounded region, replacing all O in that region with X's in place

        a region is a group of connected Os which are not on the border

        E:

        m == board.length
        n == board[i].length
        1 <= m, n <= 200
        board[i][j] is 'X' or 'O'

        if min(r,c) < 0 or r > ROWS or c > COLS or (r, c) in visited or board[r][c] == "X":
            return

        if O has only one O neighbour and isn't on border: add to cur region


        1 x 1 -> [["X"]]
        2x2 -> [["X","O"]
                ["X","X"]]

        2x2 -> [["X","O","X","X"]
                ["X","X","X", "X"]]

        3x3 -> [["X","X", "X"],
                ["X","O", "X"],
                ["X","X", "X"]]

        3x3 -> [["X","X", "X", "X", "X"],
                ["X","O", "X", "O", "X"],
                ["X","O", "O", "O", "X"],
                ["X","X", "X", "X", "X"]]
    
        A:

        """

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def isRegion(r, c, region):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False
            if (r, c) in visited or board[r][c] == "X":
                return True

            visited.add((r, c))
            region.append((r, c))

            if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                return False

            left = isRegion(r, c - 1, region)
            up = isRegion(r - 1, c, region)
            right = isRegion(r, c + 1, region)
            down = isRegion(r + 1, c, region)

            return left and up and right and down

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == "O" and (r, c) not in visited:
                    region = []
                    if isRegion(r, c, region):
                        for x, y in region:
                            board[x][y] = "X"


        