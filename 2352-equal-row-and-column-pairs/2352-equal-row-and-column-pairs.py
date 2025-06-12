class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_map = {}

        # Count each row's frequency using a hashmap (dict)
        for row in grid:
            key = tuple(row)
            row_map[key] = row_map.get(key, 0) + 1

        res = 0
        for i in range(n):
            col = tuple(grid[j][i] for j in range(n))
            if col in row_map:
                res += row_map[col]

        return res
