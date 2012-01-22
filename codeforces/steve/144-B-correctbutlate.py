#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.18

x1, y1, x2, y2 = [int(x) for x in raw_input().split()]
num_radiators  = int(raw_input())

radiator_info = []
for _ in range(num_radiators):
    # x, y, radius
    radiator_info.append([int(x) for x in raw_input().split()])

# Add the location of each general to general_locations
general_locations = []
for x in range( min([x1, x2]), max([x1, x2])+1 ):
    for y in range( min([y1, y2]), max([y1, y2])+1 ):
        if x in [x1, x2] or y in [y1, y2]:
            general_locations.append([x, y])

cold_generals = general_locations[:]

# For each general, remove from cold_generals if near radiator
for general in general_locations:
    gen_x, gen_y = general
    for radiator in radiator_info:
        r_x, r_y, radius = radiator
        if ( (gen_x - r_x)**2 + (gen_y - r_y)**2 )**0.5 <= radius and \
                general in cold_generals:
            cold_generals.remove(general)

print len(cold_generals)
