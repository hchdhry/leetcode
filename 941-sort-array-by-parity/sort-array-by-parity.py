class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        hash = {"even":[],"odd":[]}
        output = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                hash["even"].append(nums[i])
            else:
                hash["odd"].append(nums[i])
        for num in hash["even"]:
            output.append(num)
        for num in hash["odd"]:
            output.append(num)
        return output