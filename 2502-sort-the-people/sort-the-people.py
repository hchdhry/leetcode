class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_people = sorted(zip(heights, names), reverse=True)
        return [name for _, name in sorted_people]
