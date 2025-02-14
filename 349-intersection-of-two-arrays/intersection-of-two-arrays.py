class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        hash = {}
        for num in nums1:
            hash[num] = hash.get(num,0)+1
        for num in nums2:
            hash[num] = hash.get(num,0)+1
        return list(filter(lambda X: hash[X]>1,hash))
        

        