class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym = ""
        for word in words:
            acronym+=list(word)[0]
        return s == acronym
        