class Solution:

    def makeCSV(str: str) -> list:
        output = []
        with open('day1.txt') as data:
            for line in data:
                 output.append(line.strip())

        return output

    def largerThanLast(nums: list) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1

Solution().largerThanLast(Solution().makeCSV())