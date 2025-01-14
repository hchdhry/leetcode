class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1
        key = filter(lambda x: hashmap[x] == 1,hashmap)
        return (list(key)[0])

        