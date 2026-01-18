class GridEnv:
    def __init__(self, grid, start, goal, size):
        self.size = size
        self.grid = grid
        self.start = start
        self.goal = goal
        self.agent_pos = list(start)

    def observe(self):
        return tuple(self.agent_pos), self.size
    
    def is_terminal(self):
        return tuple(self.agent_pos) == self.goal

    def step(self, action):
        if action == "DOWN":
            self.agent_pos[0] += 1
        elif action == "RIGHT":
            self.agent_pos[1] += 1

        return self.observe()