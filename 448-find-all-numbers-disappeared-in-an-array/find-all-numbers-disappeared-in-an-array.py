class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        hash = {}
        for num in nums:
            hash[num] = hash.get(num,0)+1
        for i in range(1,len(nums)+1):
            if hash.get(i,0) == 0:
                output.append(i)
        return output
