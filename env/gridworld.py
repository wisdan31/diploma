import numpy as np

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
    
    def in_bounds(self, pos):
        return (0 <= pos[0] < self.size) and (0 <= pos[1] < self.size)