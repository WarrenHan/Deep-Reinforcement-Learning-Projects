import random


class Environment:
    def __init__(self):
        '''Initalizes its internal state, which is the number
        of interactions an agent has with the environment'''
        self.steps_left = 10

    def  get_observation(self):
        '''The internal state of the environment'''
        return [0.0, 0.0, 0.0]
    
    def get_actions(self):
        '''Queries the number of possible actions an agent can take.
        In thise case it is just 1 or 0'''
        return [0, 1]
    
    def is_done(self):
        '''The environmnet indicates to the agent that
        the episode is over'''
        return self.steps_left == 0
    
    def action(self, action):
        '''This handles the action of an agent on the enviroment
        and the evironmnet's reward for that action'''
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()
    
class Agent:
    def __init__(self):
        '''initialization which keeps track of the
        total rewards the agent gets'''
        self.total_reward = 0.0

    def step(self, env):
        '''the actions the agent takes
        it takes in information about the environment
        the actions it can take
        the reward the agent gets from the environment
        the total reward the agent gets (which is random in this case)'''
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_reward += reward

if __name__ == "__main__":
    '''runs the code'''
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)
    
    print("Total reward got : %.4f" % agent.total_reward)