from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        
        triangle = [[1]]
        
        for row_num in range(1, numRows):
            row = [1]  
            prev_row = triangle[row_num - 1]
            
           
            for j in range(1, row_num):
                row.append(prev_row[j - 1] + prev_row[j])
            
            row.append(1)
            triangle.append(row)
        
        return triangle
