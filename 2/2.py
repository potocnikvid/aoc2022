f = open('input.txt', 'r')
lines = f.readlines()
f.close()

score = 0
for line in lines:
    line = line.strip()
    opponent = line.split(" ")[0]
    result = line.split(" ")[1]

    rock = (result == 'X' and opponent == 'B') or (result == 'Y' and opponent == 'A') or (result == 'Z' and opponent == 'C')
    paper = (result == "X" and opponent == "C") or (result == "Y" and opponent == "B") or (result == "Z" and opponent == "A")
    scissors = (result == "X" and opponent == "A") or (result == "Y" and opponent == "C") or (result == "Z" and opponent == "B")

    if result == "X":
        score = score + 0
    elif result == "Y":
        score = score + 3
    elif result == "Z":
        score = score + 6


    if rock:
        score = score + 1
    elif paper:
        score = score + 2
    elif scissors:
        score = score + 3

print(score)
