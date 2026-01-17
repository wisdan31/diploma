from env.gridworld import Grid
from agents.agent import Agent
from policies.sweep import SweepPolicy
from experiments.simple import simple_experiment

SIZE = 10
env = Grid(SIZE)
agent = Agent([1, 1])
policy = SweepPolicy()
finish = [SIZE - 1, SIZE - 1]

result = simple_experiment(agent, finish, policy, env)
print("Found finish at", result)


