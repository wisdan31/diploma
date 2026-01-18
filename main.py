from env.gridworld import GridEnv
from agents import Agent 
from policies import SweepPolicy   
import numpy as np

grid = np.zeros((10, 10), dtype=int)



env = GridEnv(grid, (0, 0), (9, 9), 10)
agent = Agent(SweepPolicy())

def run_experiment(agent, env):
    while not env.is_terminal():
        observation = env.observe()
        action = agent.act(observation)
        env.step(action)

    print("Finished at", env.agent_pos)


run_experiment(agent, env)