f = open('input.txt', 'r')
input = f.readlines()
f.close()

forest = []
for line in input:
    forest.append([int(tree) for tree in line.strip()])

count = 0
highest_in_row = {}
highest_in_col = {}
for ix, row in enumerate(forest):
    highest_in_row[ix] = row[0]

for ix, col in enumerate(forest[0]):
    highest_in_col[ix] = col


max_scenic_score = 0
scenic_score = 0


for ix_row, treeline in enumerate(forest):
    for ix_col, tree in enumerate(treeline):
        left = 0
        for col in range(ix_col - 1, -1, -1):
            if treeline[col] >= tree:
                left += 1 
                break
            else:
                left += 1

        top = 0
        for row in range(ix_row - 1, -1, -1):
            if forest[row][ix_col] >= tree:
                top += 1
                break
            else:
                top += 1

        right = 0
        for col in range(ix_col + 1, len(treeline)):
            if treeline[col] >= tree:
                right += 1
                break
            else:
                right += 1

        bottom = 0
        for row in range(ix_row + 1, len(forest)):
            if forest[row][ix_col] >= tree:
                bottom += 1
                break
            else:
                bottom += 1

        scenic_score = left * top * right * bottom
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)