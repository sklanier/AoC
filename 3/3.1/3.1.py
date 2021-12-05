class Solution:
    def makeCSV() -> list:
        output = []
        with open('3/3.1/3.1.txt') as data:
            for line in data:
                 output.append(line.strip())

        return(output)

    def countBits(list):
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0
        c10 = 0
        c11 = 0
        c12 = 0

        for num in list:
            c1 += int(num[0])
            c2 += int(num[1])
            c3 += int(num[2])
            c4 += int(num[3])
            c5 += int(num[4])
            c6 += int(num[5])
            c7 += int(num[6])
            c8 += int(num[7])
            c9 += int(num[8])
            c10 += int(num[9])
            c11 += int(num[10])
            c12 += int(num[11])

        print(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12)
        print(int("110100010101", 2))
        print(int("001011101010", 2))
        print(3349 * 746)

data = Solution.makeCSV()
Solution.countBits(data)