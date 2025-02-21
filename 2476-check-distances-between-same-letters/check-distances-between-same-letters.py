class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hash = defaultdict(list) 
        for i in range(len(s)):
            hash[s[i]].append(i)
        x = 0
        for key,val in hash.items():
            difference = (val[1] - val[0])-1
            expected_index = ord(key) - ord('a')
            if difference != distance[expected_index]:
                return False
            x+=1
        return True
       
        