class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = {}
        hash2 = {}
        output = []
        for num in nums1:
            hash1[num] = hash1.get(num,0)+1
        for num in nums2:
            hash2[num] = hash2.get(num,0)+1
        print(hash1,hash2)
        for key,value in hash1.items():
            if hash1[key]>0 and hash2.get(key,0)>0:
                for i in range(min(hash1[key],hash2[key])):
                    output.append(key)
        return output
