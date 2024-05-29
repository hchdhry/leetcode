class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        output = 0
        while left <= right:
            if height[left] < height[right]:
                containerVolume = height[left] * (right - left)
                left += 1
            else:
                containerVolume = height[right] * (right - left)
                right -= 1
            output = max(output, containerVolume)
        return output