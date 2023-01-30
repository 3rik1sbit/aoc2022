f = open("input.txt", "r")
lines = f.readlines()

count = 0
elves = [[0, 0], [0, 0]]
for line in lines:
    elves[0][0] = int(line[0: line.find('-')])
    elves[0][1] = int(line[line.find('-')+1: line.find(',')])
    elves[1][0] = int(line[line.find(',')+1: line.rfind('-')])
    elves[1][1] = int(line[line.rfind('-')+1:len(line)].strip('\n'))

    if (elves[0][0] <= elves[1][0] and elves[0][1] >= elves[1][1]):
        count += 1
    elif (elves[0][0] >= elves[1][0] and elves[0][1] <= elves[1][1]):
        count += 1
    elif (elves[0][0] <= elves[1][0] and elves[0][1] >= elves[1][0]):
        count += 1
    elif (elves[0][0] <= elves[1][1] and elves[0][1] >= elves[1][1]):
        count += 1
print(count)
