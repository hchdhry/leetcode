class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        triangle = [[1]]
        
        for row_num in range(1, rowIndex+1):
            row = [1]  
            prev_row = triangle[row_num - 1]
            
           
            for j in range(1, row_num):
                row.append(prev_row[j - 1] + prev_row[j])
            
            row.append(1)
            triangle.append(row)
        return triangle[-1]
        