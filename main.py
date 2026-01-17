import numpy as np

SIZE = 10

grid = np.zeros((SIZE, SIZE), dtype=int)


start = [0,0]

finish = [SIZE, SIZE]

def simpleAlgorithm(start, finish):
    while True:
        current = start
        if (current == finish):
            print("Found finish")
            return

        if (start[1] < SIZE):
            start[1] += 1
        else:
            start[0] += 1

simpleAlgorithm(start, finish)
