class Solution:
    def countSeniors(self, details: List[str]) -> int:
        output = 0
        for x in details:
            age = x[11:13]
            if int(age)>60:
                output+=1
        return output
        