class Solution:
    def makeCSV() -> list:
        output = []
        with open('1/1.2/1.2.txt') as data:
            for line in data:
                 output.append(line.strip())

        return output

    def largerThanLast(data):
        count = 0
        for i in range(0, len(data) - 3):
            if (int(data[i+1]) + int(data[i+2]) + int(data[i+3])) > (int(data[i]) + int(data[i+1]) + int(data[i+2])):
                count += 1
        print(count)
data = Solution.makeCSV()
# print(len(data))
Solution.largerThanLast(data)