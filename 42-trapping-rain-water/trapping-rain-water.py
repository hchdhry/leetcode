class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)-1
        l,r= 0,n
        res = 0
        leftmax, rightmax = height[l],height[r]
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                res += max(0,leftmax-height[l])
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                res += max(0,rightmax-height[r])
        return res

            
           