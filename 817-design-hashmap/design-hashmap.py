class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        for item in self.map:
            if item[0] == key:
                item[1] = value
                return
        self.map.append([key, value])

    def get(self, key: int) -> int:
        for item in self.map:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        for item in self.map:
            if item[0] == key:
                self.map.remove(item)
                return

                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)