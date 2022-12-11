f = open('input.txt', 'r')
lines = f.readlines()
f.close()


def item_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

score = 0
for line in lines:
    line = line.strip()
    rucksack_1, rucksack_2 = line[:len(line)//2], line[len(line)//2:]

    common_items = set(rucksack_1).intersection(set(rucksack_2))

    for item in common_items:
        score += item_priority(item)

print(score)
