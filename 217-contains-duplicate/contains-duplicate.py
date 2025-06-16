class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for num in nums:
            if seen.get(num,0)>0:
                return True
            seen[num] = seen.get(num,0)+1
        return False
        