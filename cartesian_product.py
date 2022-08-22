def calc_cartesian_product(ranges):
    points = [[]]
    for r in ranges: 
        extended_points = []
        for p in points: 
            for data in r: 
                point_copy = p.copy()
                #print("og point", point_copy)
                #print()
                point_copy.append(data)
                #print("updated point", point_copy)
                #print()
                extended_points.append(point_copy)
                #print("updated extended points", extended_points)
        points = extended_points
    return points
##
assert calc_cartesian_product([['a'],[1, 2, 3],['Y', 'Z']]) == [['a', 1, 'Y'],['a', 1, 'Z'], ['a', 2, 'Y'], ['a', 2, 'Z'], ['a', 3, 'Y'], ['a', 3, 'Z']]
assert calc_cartesian_product([['a'], [1], ['#']]) == [['a', 1, '#']]
assert calc_cartesian_product([[1, 2], ['a', 'b'], ['@', '#']]) == [[1, 'a', '@'], [1, 'a', '#'], [1, 'b', '@'], [1, 'b', '#'], [2, 'a', '@'], [2, 'a', '#'], [2, 'b', '@'], [2, 'b', '#']]
