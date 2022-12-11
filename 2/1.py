f = open('input.txt', 'r')
lines = f.readlines()
f.close()

score = 0
for line in lines:
    line = line.strip()
    opponent = line.split(" ")[0]
    me = line.split(" ")[1]

    win = (me == 'X' and opponent == 'C') or (me == 'Y' and opponent == 'A') or (me == 'Z' and opponent == 'B')
    draw = (me == "X" and opponent == "A") or (me == "Y" and opponent == "B") or (me == "Z" and opponent == "C")
    lose = (me == "X" and opponent == "B") or (me == "Y" and opponent == "C") or (me == "Z" and opponent == "A")

    if win:
        score = score + 6
    elif draw:
        score = score + 3


    if me == "X":
        score = score + 1
    elif me == "Y":
        score = score + 2
    elif me == "Z":
        score = score + 3

print(score)
