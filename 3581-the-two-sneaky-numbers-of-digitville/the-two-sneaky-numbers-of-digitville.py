class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash = {}
        output = []
        for num in nums:
            hash[num] = hash.get(num,0)+1
        return [key for key in hash if hash[key]>1]

        