import numpy as np
import random
import copy


class Game:

    # Instance variable
    maxNumNeighbors = 0

    def __init__(self, solution):
        self.currentSolution = solution
        self.n = solution.size
        for i in range(1, self.n):
            self.maxNumNeighbors += i
        self.tabuTernure = int(self.maxNumNeighbors * 0.14)
        # Only the half of the structures divided by the largest diagonal will be on use.
        self.tabuStructure = np.zeros((self.n, self.n), dtype=int)
        self.frecuencyStructure = np.zeros((self.n, self.n), dtype=int)

    def find_neighbors(self):
        candidates = []
        listOfSwaps = np.empty(shape=(0, 2))

        while len(listOfSwaps) < self.n * 2:
            positions = list(range(self.n))
            random.shuffle(positions)
            newSwap = np.sort(np.array([positions.pop(), positions.pop()]))

            if not any(np.array_equal(newSwap, swap) for swap in listOfSwaps):
                listOfSwaps = np.append(listOfSwaps, [newSwap], axis=0)
            else:
                continue

            swapValue = self.get_value_of_swap(newSwap)
            penalty = self.frecuencyStructure[newSwap[0]][newSwap[1]]

            candidates.append((newSwap, swapValue, penalty))

        candidates = np.array(candidates, dtype=[('positions', object), ('swapValue', int), ('penalty', int)])
        # The last key in the sequence is used for the primary sort order and so on.
        sortedIndices = np.lexsort((candidates['penalty'], candidates['swapValue']))
        # return np.sort(candidates, order=['swapValue', 'penalty'])
        return candidates[sortedIndices]

    def get_value_of_swap(self, swap):
        neighbor = copy.deepcopy(self.currentSolution)
        neighbor[swap[0]], neighbor[swap[1]] = self.currentSolution[swap[1]], self.currentSolution[swap[0]]
        return self.evaluate_fitness(neighbor) - self.evaluate_fitness(self.currentSolution)

    # Explanation in https://arxiv.org/pdf/1802.02006.pdf
    def evaluate_fitness(self, individual):
        t1 = 0  # Number of repetitive queens in one diagonal while seen from left corner
        t2 = 0  # Number of repetitive queens in one diagonal while seen from right corner

        f1 = np.array([individual[i] - (i + 1) for i in range(self.n)])
        f2 = np.array([(1 + self.n) - individual[i] - (i + 1) for i in range(self.n)])

        f1 = np.sort(f1)
        f2 = np.sort(f2)

        for i in range(1, self.n):
            if f1[i] == f1[i - 1]:
                t1 += 1
            if f2[i] == f2[i - 1]:
                t2 += 1

        return t1 + t2

    def accept_neighbor(self, swap):
        self.apply_swap(swap)
        self.tabuStructure[swap[0]][swap[1]] = self.tabuTernure + 1  # A 1 will be subtracted in the next step
        self.frecuencyStructure[swap[0]][swap[1]] += 1

    def apply_swap(self, swap):
        neighbor = copy.deepcopy(self.currentSolution)
        self.currentSolution[swap[0]], self.currentSolution[swap[1]] = neighbor[swap[1]], neighbor[swap[0]]

    def print_solution(self):
        result = ""
        for col in range(self.n):
            result += (str(self.currentSolution[col]) + ' ')
        print(result)
