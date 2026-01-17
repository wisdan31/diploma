def simple_experiment(agent, finish, policy, env):
    while agent.pos != finish:
        agent.step(policy.select_action(agent.pos, finish, env))
    return agent.pos