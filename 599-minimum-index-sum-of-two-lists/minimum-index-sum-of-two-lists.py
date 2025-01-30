class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash1 = {list1[i]: i for i in range(len(list1))} 
        min_sum = float('inf')
        result = []

        for j in range(len(list2)):
            if list2[j] in hash1: 
                index_sum = j + hash1[list2[j]]  
                
                if index_sum < min_sum: 
                    min_sum = index_sum
                    result = [list2[j]]
                elif index_sum == min_sum: 
                    result.append(list2[j])

        return result
