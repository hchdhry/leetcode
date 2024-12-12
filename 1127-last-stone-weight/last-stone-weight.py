class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            res = stones.pop()-stones.pop()
            if res>0:
                stones.append(res)
        if len(stones)>0:
            return stones[0]
        else:
            return 0

        