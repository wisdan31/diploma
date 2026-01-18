class Simulation:
    def __init__(self, agent, env):
        self.agent = agent
        self.env = env
        self.visited_nodes = []

    def run():
        return None
    
class SimpleSimulation(Simulation):
    def run(self):
        while not self.env.is_terminal():
            observation = self.env.observe()
            current_node = observation[0]
            self.visited_nodes.append(current_node)
            action = self.agent.act(observation)
            self.env.step(action)

        print("Finished at", self.env.agent_pos)
        print("Path of agent:", self.visited_nodes)