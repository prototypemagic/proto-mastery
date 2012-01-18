

num_of = int(raw_input())

heights = raw_input().split()

for x in range(num_of):
    heights[x] = int(heights[x])

highest = 0
lowest = 0
lp = 0

for x in range(num_of):
    if heights[x] > highest:
        highest = heights[x]
        hp = x

for x in range(num_of):
    if heights[x] < lowest and heights != 0:
        lowest = heights[x]
        lp = x

print heights
print lp,hp,highest,lowest
counter = 0

#for x in range(num_of):
#    if heights[x] == lowest:
#        lp = x
#        break
#for x in range(num_of):
#    if heights[x] == highest:
#        hp = x
#        break

while heights[0] != highest:
    hp = hp - 1
    heights.remove(highest)
    heights.insert(hp, highest)
    counter = counter+1
while heights[-1] != lowest:
    lp = lp + 1
    heights.remove(lowest)
    heights.insert(lp, lowest)
    counter = counter+1

print counter
