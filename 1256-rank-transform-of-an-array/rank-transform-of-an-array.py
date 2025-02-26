class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = arr.copy()
        output = []
        copy = list(set(copy))
        copy.sort()
        hash = {}
        for i in range(len(copy)):
            hash[copy[i]] = i+1
        for num in arr:
            output.append(hash[num])
        return output
        
        