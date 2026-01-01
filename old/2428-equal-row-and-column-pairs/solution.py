class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = list(zip(*grid))

        print(cols)

        row_counter = defaultdict(int)

        for row in grid:
            row_counter[tuple(row)] += 1

        

        count = 0
        for col in cols:
            count += row_counter[col]

        return count
