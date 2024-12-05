class TimeMap:

    def __init__(self):
        # Initialize the data structure as a dictionary
        # Each key will map to a list of (timestamp, value) pairs
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key doesn't exist, initialize it with an empty list
        if key not in self.map:
            self.map[key] = []
        # Append the (timestamp, value) pair to the list for the given key
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return an empty string
        if key not in self.map:
            return ""

        # Use binary search to find the value with the closest timestamp <= the given timestamp
        values = self.map[key]
        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                # Found a valid timestamp, save the value and move right
                result = values[mid][1]
                left = mid + 1
            else:
                # Move left
                right = mid - 1

        return result
