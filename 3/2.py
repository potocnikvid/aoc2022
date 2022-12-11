f = open('input.txt', 'r')
lines = f.readlines()
f.close()

def item_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

score = 0


# iterate over the lines three at a time
for i in range(0, len(lines), 3):
    elf1, elf2, elf3 = lines[i], lines[i+1], lines[i+2]

    # strip the newlines
    elf1, elf2, elf3 = elf1.strip(), elf2.strip(), elf3.strip()

    # get the intersection of the three sets
    badge = set(elf1).intersection(set(elf2)).intersection(set(elf3))

    # add the priority of each item in the intersection
    score += sum(item_priority(item) for item in badge)


print(score)
