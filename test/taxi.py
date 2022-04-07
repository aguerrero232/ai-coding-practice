import gym
# Basic Agent Loop
env = gym.make("Taxi-v3")
observation = env.reset()
for _ in range(1000):
    env.render()
    # your agent here (this takes random actions)
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        env.render()
        break
