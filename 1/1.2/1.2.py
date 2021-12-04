class Solution:
    def makeCSV() -> list:
        output = []
        with open('1/day1_input.txt') as data:
            for line in data:
                 output.append(line.strip())

        return output

    def largerThanLast(data):
        count = 1
        for i in range(1, len(data)):
            if data[i] > data[i-1]:
                count += 1
        print(count)
data = Solution.makeCSV()
# print(len(data))
Solution.largerThanLast(data)