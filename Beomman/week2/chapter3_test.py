import copy

r1 = ['John', ('man', 'USA'), [175,23]]
r2 = copy.deepcopy(r1)  ## deep copy
r3 = list(r1)  ## shallow copy
r4 = r1[:]  ## shallow copy

r1 is r2
r1 == r2
r1[0] is r2[0]
r1[2] is r2[2]
r1[2] == r2[2]

