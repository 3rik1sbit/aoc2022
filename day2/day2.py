f = open("input_day2.txt", "r")
lines = f.readlines()
# A = X = ROCK
# B = Y = PAPER
# C = Z = SCISSORS
points = 0
for line in lines:
    match line[2]:
        case "X":
            points += 0
            match line[0]:
                case "A":
                    points += 3
                case "B":
                    points += 1
                case "C":
                    points += 2
        case "Y":
            points += 3
            match line[0]:
                case "A":
                    points += 1
                case "B":
                    points += 2
                case "C":
                    points += 3
        case "Z":
            points += 6
            match line[0]:
                case "A":
                    points += 2
                case "B":
                    points += 3
                case "C":
                    points += 1
print(points)
