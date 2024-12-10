class TrieNode:
    def __init__(self):
        self.children = {}
        self.LastLetter = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.LastLetter = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):  
                return node.LastLetter
            char = word[i]
            if char == '.':  
                for child in node.children.values():
                    if dfs(child, i + 1):  
                        return True
                return False
            else:  
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)  

        return dfs(self.root, 0)  
