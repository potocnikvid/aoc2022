import math

f = open('input.txt', 'r')
lines = f.readlines()
f.close()


def build_towers(lines):
    num_towers = math.ceil(len(lines[0])/4)
    max_height = -1
    matrix = []
    towers = []
    for line in lines:
        max_height += 1
        if '[' in line:
            matrix.append(line)
        else:
            break

    for i in range(num_towers):
        towers.append([])

    for i in range(len(matrix)):
        print(matrix[i])
        for ix, j in enumerate(range(1, len(matrix[i]), 4)):
            towers[ix].append(matrix[i][j])
    
    return towers


def clean_towers(towers):
    for i in range(len(towers)):
        towers[i] = [x for x in towers[i] if x != ' ']
    return towers


def parse_moves(lines):
    moves = []
    for line in lines:
        if 'move' not in line:
            continue
        (move, _from, to) = int(line.split(' ')[1]), int(line.split(' ')[3]), int(line.split(' ')[5])
        moves.append([move, _from - 1, to - 1])
    return moves

def move_many(towers, move_count, _from, to):
    towers[to] = towers[_from][0:move_count] + towers[to]
    towers[_from] = towers[_from][move_count:]
    return towers 

a = build_towers(lines)
towers = clean_towers(a)
print(towers)
moves = parse_moves(lines)

for move in moves:
    towers = move_many(towers, move[0], move[1], move[2])

print(towers)
