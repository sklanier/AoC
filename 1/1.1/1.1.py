class Solution:
    def makeCSV() -> list:
        output = []
        with open('1/1.1/1.1.txt') as data:
            for line in data:
                 output.append(line.strip())

        return output

    def largerThanLast(data):
        count = 0
        for i in range(1, len(data)):
            if int(data[i]) > int(data[i-1]):
                count += 1
        print(count)
data = Solution.makeCSV()
# print(len(data))
Solution.largerThanLast(data)