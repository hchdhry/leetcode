class Trie:

    def __init__(self):
        self.array = []
        

    def insert(self, word: str) -> None:
        self.array.append(word)

        

    def search(self, word: str) -> bool:
        for i in range(len(self.array)):
            if word == self.array[i]:
                return True
        return False
        

        

    def startsWith(self, prefix: str) -> bool:
        for i in range(len(self.array)):
            potentialPrefix = self.array[i][:len(prefix)]
            if prefix == potentialPrefix:
                return True
            
        return False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)