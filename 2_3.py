import gym
from typing import TypeVar
import random

Action = TypeVar('Action')
class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon = 0.1):
        super().__init__(env)
        self.epsilon = epsilon

    def action(self, action: Action) -> Action:
        if random.random() < self.epsilon:
            print('Random')
            return self.env.action_space.sample()
        return action

    
if __name__ == "__main__":
    env = RandomActionWrapper(gym.make("CartPole-v0"))
    obv = env.reset()
    total_reward = 0.0
    while True:
        obs, reward, done, _, _ = env.step(0)
        total_reward += reward
        if done:
            break
    print(f"Reward got: {total_reward}") 
    