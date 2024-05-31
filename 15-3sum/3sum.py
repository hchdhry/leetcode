class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedList = sorted(nums)
        output = []
        n = len(sortedList)

        for x in range(n - 2):
            # Skip duplicates for x
            if x > 0 and sortedList[x] == sortedList[x - 1]:
                continue

            y, z = x + 1, n - 1

            while y < z:
                total = sortedList[x] + sortedList[y] + sortedList[z]

                if total < 0:
                    y += 1
                elif total > 0:
                    z -= 1
                else:
                    output.append([sortedList[x], sortedList[y], sortedList[z]])

                  
                    while y < z and sortedList[y] == sortedList[y + 1]:
                        y += 1

                   
                    while y < z and sortedList[z] == sortedList[z - 1]:
                        z -= 1

                    y += 1
                    z -= 1

        return output