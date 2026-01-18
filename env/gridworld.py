class GridEnv:
    def __init__(self, size):
        self.size = size
        self.agent_pos = [0, 0]

    def observe(self):
        return tuple(self.agent_pos), self.size

    def step(self, action):
        if action == "DOWN":
            self.agent_pos[0] += 1
        elif action == "RIGHT":
            self.agent_pos[1] += 1
