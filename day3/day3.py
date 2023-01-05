def charToValue(char):
    ascii = ord(char)
    if ascii < 97:
        return ascii - 38
    else:
        return ascii - 96


f = open("input.txt", "r")
lines = f.readlines()

value = 0
i = 0
elves = [""] * 3

for line in lines:
    elves[i % 3] = line.rstrip('\n')
    i += 1
    if i % 3 == 0:
        s = str(set(elves[0]) & set(elves[1]) & set(elves[2]))
        value += charToValue(s[2])
print(value)
