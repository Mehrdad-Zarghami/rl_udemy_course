import random

# """
# The simplicity of the preceding code illustrates the important basic concepts that come from
# the RL model. The environment could be an extremely complicated physics model, and an
# agent could easily be a large neural network (NN) that implements the latest RL algorithm, but
# the basic pattern will stay the same – on every step, the agent will take some observations from
# the environment, do its calculations, and select the action to take. The result of this action will
# be a reward and a new observation.

# """
class Environment:
    def __init__(self):
        self.steps_left = 10

    def get_observations(self)-> list[float]: 
        """
        The get_observation() method is supposed to return the current environment's observation
        to the agent. It is usually implemented as some function of the internal state of the environment.  
        
        In our example, the observation vector is always zero, as the environment basically has no internal state.
        """
        return [0.0, 0.0, 0.0]
    
    def get_actions(self) -> list[int]:
        """
        The get_actions() method allows the agent to query the set of actions it can execute.
        Normally, the set of actions that the agent can execute does not change over time, but some actions can become impossible in different states (for example, not every move is possible in any
        position of the tic-tac-toe game). In our simplistic example, there are only two actions that the
        agent can carry out, which are encoded with the integers 0 and 1
        """
        return [0, 1]
    
    def is_done(self) -> bool:
        """
        The preceding method signaled the end of the episode to the agent
        """
        return self.steps_left == 0
    
    def action(self, action:int) -> float:
        """
            The action() method is the central piece in the environment's functionality. It does two
            things – handles an agent's action and returns the reward for this action. In our example, the
            reward is random and its action is discarded. Additionally, we update the count of steps and
            refuse to continue the episodes that are over.
        """
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1 
        return random.random()

class Agent:
    """
    The step function accepts the environment instance as an argument
    and allows the agent to
    perform the following actions:
        *Observe the environment
        *Make a decision about the action to take based on the observations
        *Submit the action to the environment
        *Get the reward for the current step

    For our example, the agent is dull and ignores the observations
    obtained during the decision making process about which action to take.
    Instead, every action is selected randomly. The final piece is the glue code,
    which creates both classes and runs one episode:
    """
    def __init__(self) -> None:
        self.total_reward = 0.0

    def step(self, env: Environment)  -> None:
        current_obs = env.get_observations()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_reward += reward

if __name__ == "__main__":
    env = Environment()
    agent = Agent()
    while not env.is_done():
        agent.step(env)

    print(f"Total reward got: {agent.total_reward}")

