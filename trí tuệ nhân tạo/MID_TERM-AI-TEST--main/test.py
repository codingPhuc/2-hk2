print(('this',6))
a= list()
a.append(((4,1),'this'))

print(((4,1),'this') in a)
print(a[0][0])


def get_directions(locations):
    directions = []
    for i in range(1, len(locations)):
        curr = locations[i]
        prev = locations[i-1]
        if curr[0] > prev[0]:
            directions.append("S")
        elif curr[0] < prev[0]:
            directions.append("N")
        elif curr[1] > prev[1]:
            directions.append("E")
        elif curr[1] < prev[1]:
            directions.append("W")
    directions.append("Stop")
    return directions


locations = [(3, 11), (3, 12), (3, 13), (4, 13), (5, 13), (5, 12), (6, 12), (7, 12), (7, 11), (7, 10), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1)]
directions = get_directions(locations)
print(directions)


