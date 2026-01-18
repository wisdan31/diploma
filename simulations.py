class Simulation:
    def __init__(self, agent, env):
        self.agent = agent
        self.env = env

    def run():
        return None
    
class SimpleSimulation(Simulation):
    def run(self):
        while not self.env.is_terminal():
            observation = self.env.observe()
            action = self.agent.act(observation)
            self.env.step(action)

        print("Finished at", self.env.agent_pos)