r1 = [1,2,3,[4,5]]
r2 = [x for x in r1]
r1 is r2
r1[0] is r2[0]
r1[2] is r2[2] ## shallow copy
