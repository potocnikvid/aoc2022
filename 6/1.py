import math
from collections import deque

f = open('input.txt', 'r')
input = f.readlines()[0]
f.close()

start_marker_length = 4

possible_markers = [input[i:i+start_marker_length] for i in range(len(input)-2)]
print(possible_markers)

for ix, marker in enumerate(possible_markers):
    if len(set(marker)) == start_marker_length:
        print(ix + 4, marker)
        break