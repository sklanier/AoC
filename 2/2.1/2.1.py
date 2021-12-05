class Solution:
    def makeCSV() -> list:
        output = []
        with open('2/2.1/2.1.txt') as data:
            for line in data:
                 output.append(line.strip())

        return output
    
    def countDisplacement(list):
        y = 0
        x = 0

        for command in list:
            if command.split(' ')[0] == 'forward':
                x += int(command.split(' ')[1])
            if command.split(' ')[0] == 'down':
                y += int(command.split(' ')[1])
            if command.split(' ')[0] == 'up':
                y -= int(command.split(' ')[1])
        
        print(x * y)
                
                

data = Solution.makeCSV()
Solution.countDisplacement(data)