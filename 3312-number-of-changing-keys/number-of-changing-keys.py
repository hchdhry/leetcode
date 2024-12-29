class Solution:
    def countKeyChanges(self, s: str) -> int:
        prev = None
        output = 0

        for chara in s:
            if prev is not None and chara.isalpha() and chara.lower() !=  prev.lower():
                output+=1
            prev = chara
        return output


        