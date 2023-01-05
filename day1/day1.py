f = open("input_day1.txt", "r")
lines = f.readlines()
elves = 1
for line in lines:
    if line.strip() == "":
        elves += 1
capacities = [0] * elves
i = 0

for line in lines:
    if line.strip() == "":
        i += 1
    else:
        capacities[i] += int(line)
elf_1 = max(capacities)
capacities = list(filter(lambda capacity: capacity != elf_1, capacities))
elf_2 = max(capacities)
capacities = list(filter(lambda capacity: capacity != elf_2, capacities))
elf_3 = max(capacities)
print(elf_1 + elf_2 + elf_3)
