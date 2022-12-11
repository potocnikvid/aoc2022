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

print(highest_in_row)
print(highest_in_col)

    
for ix_row, treeline in enumerate(forest):
    for ix_col, tree in enumerate(treeline):
        # print(ix_row, ix_col, tree)
        if ix_row == 0 or ix_col == 0 or ix_row == len(forest) - 1 or ix_col == len(treeline) - 1:
            count += 1
        elif tree > highest_in_row[ix_row]:
            print('row')
            count += 1
            highest_in_row[ix_row] = tree
            if tree > highest_in_col[ix_col]:
                highest_in_col[ix_col] = tree
        elif tree > highest_in_col[ix_col]:
            print('col')
            count += 1
            highest_in_col[ix_col] = tree
            if tree > highest_in_row[ix_row - 1]:
                highest_in_row[ix_row - 1] = tree
        elif tree > max(treeline[ix_col + 1:]):
            print('row forward')
            print(treeline[ix_col + 1:])
            count += 1
        elif tree > max([forest[ix][ix_col] for ix in range(ix_row + 1, len(forest))]):
            print('col forward')
            print([forest[ix][ix_col] for ix in range(ix_row + 1, len(forest))])
            count += 1



print(count)	