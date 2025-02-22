class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash = defaultdict(lambda: [0, -1])

   
        for i, (start, end) in enumerate(paths):
            hash[start][0] += 1 
            hash[start][1] = i    
            if end not in hash: 
                hash[end] = [0, i]  

        dest = ""
        max_index = -1
        for city, (count, index) in hash.items():
            if count == 0 and index > max_index: 
                dest = city
                max_index = index

        return dest
