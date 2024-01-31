import gym
import random

#Wrappers and Monitors
#Applying a wrapper to replace actions with random values
#Done by overriding the parent's class 
class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon=0.1):
        super(RandomActionWrapper, self).__init__(env)
        self.epsilon = epsilon

    def action(self, action):
        if random.random() < self.epsilon:
            print("Random!")
            return self.env.action_space.sample()
        return action


if __name__ == "__main__":
    env = RandomActionWrapper(gym.make("CartPole-v1"))
    total_reward = 0.0
    total_steps = 0
    obs = env.reset()


#This loop samples a random action and returns the next observation, reward, and done flag. This continues until the
#training episode is over
while True:
    action = env.action_space.sample()
    obs, reward, done, _, __ = env.step(action) #In the action space, each step returns a tuple of three values
    total_reward += reward
    total_steps += 1
    if done:
        break

print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))

    

