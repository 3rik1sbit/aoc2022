f = open("input.txt", "r")
lines = f.readlines()
line = lines[0]

length = len(line)

for i in range(13, length):
    if len(set(line[i-14:i])) == 14:
        break

print(i)
