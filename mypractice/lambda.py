add10 = lambda x: x+10
print(add10(5))

point2D = [(1,2), (15,1), (5,-1), (10,4)]
point2D_sorted = sorted(point2D)
point2D_sorted_by_secIndex = sorted(point2D, key = lambda x: x[1])

print(point2D_sorted) #[(1, 2), (5, -1), (10, 4), (15, 1)]
print(point2D_sorted_by_secIndex) #[(5, -1), (15, 1), (1, 2), (10, 4)]


