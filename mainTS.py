from exceptions import *
from game import *
import time
import numpy as np
import copy
from math import exp


try:
    n = int(input("Write a number greater than 3 to be the board dimension and press (Enter)\n"))
    if n < 4:
        raise LessThanFourError(n)

except ValueError as err:
    exit("The value must be an integer.")
except LessThanFourError as err:
    exit(str(err))


strg = input("Type a solution for the {}-queens problem and press (Enter)\n".format(n))

try:
    initialSolution = np.fromiter(map(int, strg.split(' ')), dtype=int)

    if initialSolution.size != n:
        raise IncorrectInputLengthError(n)

    if np.min(initialSolution) < 0 or np.max(initialSolution) > n:
        raise IncorrectInputError(n)

    if initialSolution.size != np.unique(initialSolution).size:
        raise DuplicateValuesError(n)

except IncorrectInputLengthError as err:
    exit(str(err))
except IncorrectInputError as err:
    exit(str(err))
except DuplicateValuesError as err:
    exit(str(err))
except ValueError as err:
    exit("The characters in the solution must be integers between 0 and {}.".format(n))

# ----------------------------------------------------------------------------------------------------- #

game = Game(initialSolution)
solutions = np.empty(shape=(0, game.n), dtype=int)

beginning, lastFound = time.time(), time.time()
while time.time() - beginning < 60. and time.time() - lastFound < float(game.n * 2):
    neighbors = game.find_neighbors()

    # Choose new solution among neighbors
    for neighbor in neighbors:
        swap = neighbor[0]
        swapValue = neighbor[1]
        # Accept swap if it is not tabu or aspiration criteria
        if game.tabuStructure[swap[0]][swap[1]] == 0 or swapValue < 0:
            game.accept_neighbor(swap)
            break

    for index, tabuSwap in np.ndenumerate(game.tabuStructure):
        if tabuSwap != 0:
            game.tabuStructure[index[0]][index[1]] -= 1

    if game.evaluate_fitness(game.currentSolution) is 0:
        if not any(np.array_equal(game.currentSolution, solution) for solution in solutions):
            game.print_solution()
            solutions = np.append(solutions, [copy.deepcopy(game.currentSolution)], axis=0)
            lastFound = time.time()
        # Restart game
        game.tabuStructure = np.zeros((game.n, game.n), dtype=int)
        game.frecuencyStructure = np.zeros((game.n, game.n), dtype=int)
        game.currentSolution = np.arange(1, game.n + 1)
        np.random.shuffle(game.currentSolution)

print('Number of solutions in {} seconds: {}'.format(lastFound - beginning, len(solutions)))

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
