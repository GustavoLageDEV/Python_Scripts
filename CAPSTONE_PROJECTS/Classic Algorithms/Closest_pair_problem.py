#!/usr/bin/env python
# coding: utf-8

# **Closest pair problem** - The closest pair of points problem or closest pair problem is a problem of computational geometry: given *n* points in metric space, find a pair of points with the smallest distance between them. 
# [[dabillox (Python)]](https://github.com/dabillox/pyprojects/blob/master/closestpairproblem.py) 
# [[liuyang1 (Python)]](https://github.com/liuyang1/Projects/blob/master/Classic%20Algorithms/cloestpair.py) 
# [[smac89 (C++)]](https://github.com/smac89/Projects/tree/master/solutions/classic-algorithms/closestpair) 
# [[sijunhe (java)]](https://github.com/sijunhe/Project-Programs/tree/master/java/closest%20Pair)

# d=√((x_2-x_1)²+(y_2-y_1)²)

all_points = [(1,5),(2,7),(8,3),(5,5)]
min_dist = 999999

for point in all_points:
    
     for i in range(len(all_points)):
         
        x1 = point[0]
        y1 = point[1]
        x2 = all_points[i][0]
        y2 = all_points[i][1]

        dist = ((x2-x1)**2 +(y2-y1)**2)**0.5

        if dist < min_dist and dist != 0:
            min_dist = dist
            point1 = point
            point2 = all_points[i]

print(f"The closest pair of point from {all_points} are: {point1} and {point2} with a distance of {round(min_dist,3)}")