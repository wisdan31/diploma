from env.gridworld import GridEnv
from agents import Agent 
from policies import SweepPolicy   
from simulations import SimpleSimulation
import numpy as np

grid = np.zeros((10, 10), dtype=int)
env = GridEnv(grid, (0, 0), (9, 9), 10)
agent = Agent(SweepPolicy())
sim01 = SimpleSimulation(agent, env)

sim01.run()