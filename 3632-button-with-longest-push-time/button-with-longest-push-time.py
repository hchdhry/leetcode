class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:

        res = [0, 0]
        prev = 0

        for i, t in events:
            curr_time = t - prev
            if curr_time > res[1] or (curr_time == res[1] and i < res[0]):
                res = [i, curr_time]
            prev = t

        return res[0]