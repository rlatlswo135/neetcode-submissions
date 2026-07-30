class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
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
                    print('num',num,x,y,areas,point)
                    print(num in rows[x],num in cols[y],num in areas[point])
                    return False
                
                rows[x].append(num)
                cols[y].append(num)
                areas[point].append(num)


        return True
        