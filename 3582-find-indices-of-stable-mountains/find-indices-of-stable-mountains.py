class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        output = []
        doNothing = 0
        for i in range(len(height)):
            if i == 0:
                doNothing +=1
            elif height[i-1]>threshold:
                output.append(i)
        return output
            
            

        