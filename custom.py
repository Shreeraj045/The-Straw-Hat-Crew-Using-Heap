# You can add any additional function and class you want to implement in this file
from treasure import Treasure
class Inter_treasure:
    def __init__(self,treasure:Treasure):
                self.id = treasure.id
                self.size = treasure.size
                self.arrival_time = treasure.arrival_time
                self.completion_time = None

                self.curr_size = treasure.size

