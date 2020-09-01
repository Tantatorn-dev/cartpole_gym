import gym
from agent import QAgent

env = gym.make('CartPole-v0')

agent = QAgent(env)
agent.train()
t = agent.run()
print("Time", t)