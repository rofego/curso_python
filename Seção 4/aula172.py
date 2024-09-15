# count é um iterador sem fim

from itertools import count

c1 = count()
r1 = range(100)

print(next(c1))
print(next(c1))

# for i in r1:
#     print(next(c1))

print('c1',hasattr(c1, '__iter__'))
print('c1', hasattr(c1,'__next__'))
print('r1',hasattr(r1, '__iter__'))
print('r1', hasattr(r1,'__next__'))