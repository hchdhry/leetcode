class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,column = len(board), len(board[0])
        visited = set()

        def traverse(x,y,i):
            if i == len(word):
                return True
            if x>=row or y>=column or x<0 or y<0 or (x,y) in visited or word[i] != board[x][y]:
                return False 
            visited.add((x,y))
            res =(
            traverse(x+1,y,i+1) or
            traverse(x-1,y,i+1) or
            traverse(x,y+1,i+1) or 
            traverse(x,y-1,i+1)
            )
            visited.remove((x, y))
            return res
        
        for r in range(row):
            for c in range(column):
                if traverse(r, c, 0):
                    return True
        return False
            
        