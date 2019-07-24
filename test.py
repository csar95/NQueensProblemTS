import numpy as np
import random


x = np.arange(10)
np.roll(x, 2)

print(np.zeros(4, dtype=int))

candidates = [(np.array([1,2]), -1, 0), (np.array([7,4]), 1, 1), (np.array([7,4]), -1, 1)]
print(candidates)

penalty = 1
swapValue = -1
if swapValue in np.array(candidates, dtype=[('positions', object), ('swapValue', int), ('penalty', int)])['swapValue']:
    penalty += 1
candidates.append((np.array([1,3]), swapValue, penalty))

candidates = np.array(candidates, dtype=[('positions', object), ('swapValue', int), ('penalty', int)])
print(candidates['swapValue'])

print(np.sort(np.array([1, -1, 1])))

print(np.sort(candidates, order=['swapValue', 'penalty']))



positions = list(range(2))
random.shuffle(positions)
print(np.array([positions.pop(), positions.pop()]))

c = np.array([[1,2,3],[4,5,6]])
#for x in np.nditer(c):
    #print(x)

candidates = np.empty(shape=(0, 3), dtype=[('positions', object), ('swapValue', int), ('penalty', int)])
candidates = np.append(candidates, [(np.array([1,2]), 1, 0)], axis=0)
candidates = np.append(candidates, [(np.array([7,4]), -1, 0)], axis=0)
print(candidates)




surnames =    ('Hertz',    'Hertz', 'Galilei')
first_names = ('Heinrich', 'Galileo', 'Galileo')
ind = np.lexsort((first_names, surnames))
print(ind)

candidates = [(np.array([1,2]), -1, 0), (np.array([1,2]), 1, 3), (np.array([7,4]), 1, 1), (np.array([7,4]), -1, 1), (np.array([7,4]), -1, 1), (np.array([7,4]), 2, 0)]
candidates = np.array(candidates, dtype=[('positions', object), ('swapValue', int), ('penalty', int)])
ind1 = np.lexsort((candidates['penalty'],candidates['swapValue']))
print(ind1)
sorted_candidates = candidates[ind1]
print(sorted_candidates)


# tabuStructure = np.zeros((8,8), dtype=int)
# for i, t in np.ndenumerate(tabuStructure):
#     print('{}_{}'.format(i[0], t))

