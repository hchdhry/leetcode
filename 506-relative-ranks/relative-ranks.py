class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        copy = score.copy()
        copy.sort(reverse=True)
        output = []
        hash = {}
        for i in range(len(copy)):
            if i == 0:
                hash[copy[i]] = "Gold Medal"
            elif i == 1:
                hash[copy[i]] = "Silver Medal"
            elif i == 2:
                hash[copy[i]] = "Bronze Medal"
            else:
                hash[copy[i]] = f"{i+1}"
        for i in range(len(score)):
            output.append(hash[score[i]])
        return output
            


        
       
        