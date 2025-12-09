class RewardMaps:
    def __init__(self):
        self.reward_maps = {}

    def set_reward_map(self, env_number, reward_map):
        self.reward_maps[env_number] = reward_map

    def get_reward_map(self, env_number):
        return self.reward_maps[env_number]



reward_maps = RewardMaps()
