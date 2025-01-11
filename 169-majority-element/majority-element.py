class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for number in nums:
            hashmap[number] = hashmap.get(number,0)+1 

        key_with_max_value = max(hashmap, key=hashmap.get)
        return key_with_max_value
        
        