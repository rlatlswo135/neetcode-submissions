class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        areas = {
            "00":[],
            "01":[],
            "02":[],
            "10":[],
            "11":[],
            "12":[],
            "20":[],
            "21":[],
            "22":[],
        }

        for x,row in enumerate(board):
            for y,num in enumerate(row):
                if num == ".":
                    continue
                
                point = str(x//3) + str(y//3)
                if num in rows[x] or num in cols[y] or num in areas[point]:
                    return False
                
                rows[x].add(num)
                cols[y].add(num)
                areas[point].append(num)


        return True
        