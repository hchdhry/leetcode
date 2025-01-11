class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    
        toString = "".join(map(str, digits))
        res = int(toString) + 1
        
        
        return [int(digit) for digit in str(res)]
