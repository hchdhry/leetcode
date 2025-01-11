class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        toString = ""
        for number in digits:
            toString += (str(number))
        res = int(toString) + 1
        toString = str(res)
        for char in toString:
            output.append(int(char))
        return output
            
        