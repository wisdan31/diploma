class Policy:
    def select(self, observation):
        raise NotImplementedError

class SweepPolicy(Policy):
    def select(self, observation):
        pos, size = observation
        
        if pos[0] < size-1:
            return "DOWN"
        elif pos[1] < size-1:
            return "RIGHT"
        
        return None