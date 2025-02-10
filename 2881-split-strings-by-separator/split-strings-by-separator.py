class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answ=[]
        for word in words:
            for w in word.split(separator):
                if w:
                    answ.append(w)
        return answ        