class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1
        key = next((k for k in hashmap if hashmap[k] == 1), None)
        return key

        