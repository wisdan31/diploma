class Agent:
    def __init__(self, start):
        self.pos = start.copy()

    def step(self, action):
        if action == "RIGHT":
            self.pos[1] += 1
        elif action == "DOWN":
            self.pos[0] += 1