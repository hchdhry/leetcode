class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash = {}
        output = []
        for num in nums:
            hash[num] = hash.get(num,0)+1
        return list(filter(lambda x: hash[x]>1,hash))

        