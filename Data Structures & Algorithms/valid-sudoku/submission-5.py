class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        areas = [set() for _ in range(9)]

        for x,row in enumerate(board):
            for y,num in enumerate(row):
                if num == ".":
                    continue
                
                point = (x//3) * 3 + y//3
                if num in rows[x] or num in cols[y] or num in areas[point]:
                    return False
                
                rows[x].add(num)
                cols[y].add(num)
                areas[point].add(num)


        return True
        