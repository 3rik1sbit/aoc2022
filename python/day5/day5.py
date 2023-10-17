f = open("input.txt", "r")
lines = f.readlines()

for i, line in enumerate(lines):
    if line.find('1') != -1:
        length = int(line.strip()[-1])
        height = i
        break

stacks = [''] * length

for i in range(height):
    line = lines[i]
    for x in range(length):
        a = (4*x)+1
        if line[a] != " ":
            stacks[x] += line[a]

for i, stack in enumerate(stacks):
    stacks[i] = stack[::-1]

for i, line in enumerate(lines):
    if i >= height + 2:
        split_instructions = line.strip().split(" ")
        from_stack_index = int(split_instructions[3])-1
        to_stack_index = int(split_instructions[5])-1
        amount_of_crates_to_move = int(split_instructions[1])
        crates_to_move = stacks[from_stack_index][-amount_of_crates_to_move:]
        stacks[to_stack_index] += crates_to_move
        stacks[from_stack_index] = stacks[from_stack_index][:len(
            stacks[from_stack_index])-amount_of_crates_to_move]


print(stacks)
