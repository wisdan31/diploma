class SweepPolicy:
    def select_action(self, agent_pos, finish, env):
        if agent_pos[0] < env.size - 1:
            return "DOWN"
        elif agent_pos[1] < env.size - 1:
            return "RIGHT"
        return None  