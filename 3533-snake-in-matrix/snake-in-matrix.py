class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        output = 0
        for command in commands:
            if command == "RIGHT":
                output+=1
            if command == "DOWN":
                output+=n
            if command == "UP":
                output -= n
            if command == "LEFT":
                output -=1
        return output


        