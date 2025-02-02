class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1 

        n = len(words)
        queue = deque([(startIndex, 0)]) 
        visited = set([startIndex])  

        while queue:
            index, steps = queue.popleft()

            if words[index] == target:
                return steps  

            for new_index in [(index + 1) % n, (index - 1) % n]:
                if new_index not in visited:
                    visited.add(new_index)
                    queue.append((new_index, steps + 1))

        return -1 
