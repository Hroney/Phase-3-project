# from models.player.Player import Player
# from models.campaign.Campaign import Campaign
# from models.player_campaign._Player_Campaign import PlayerCampaignMethods

# class PlayerCampaign(PlayerCampaignMethods):
    
#     all = {}

#     def __init__(self, player, campaign):
#         self.player = player
#         self.campaign = campaign

#     @property
#     def player(self):
#         return self._player
    
#     @player.setter
#     def player(self, player):
#         if isinstance(player, int) and Player.find_by_id(player):
#             self._player = player
#         else:
#             raise ValueError(
#                 "Can't find Player / Not a valid ID number"
#             )
    
#     @property
#     def campaign(self):
#         return self._campaign
    
#     @campaign.setter
#     def campaign(self, campaign):
#         if isinstance(campaign, int) and Campaign.find_by_id(campaign):
#             self._campaign = campaign
#         else:
#             raise ValueError(
#                 "Can't find Campaign / Not a valid ID number"
#             )