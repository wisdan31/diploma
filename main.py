from env.gridworld import GridEnv
from agents import Agent 
from policies import SweepPolicy   

env = GridEnv(10)
agent = Agent(SweepPolicy())

while env.agent_pos != [9, 9]:
    obs = env.observe()
    action = agent.act(obs)
    env.step(action)

print("Finished at", env.agent_pos)
