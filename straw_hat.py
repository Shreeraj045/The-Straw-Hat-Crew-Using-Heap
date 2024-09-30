'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure

class StrawHatTreasury:
    def __init__(self, m):
        self.number = m
        self.crew_heap = Heap(self.compare_func1,[])
        for i in range(m):
            self.crew_heap.insert(CrewMate())
        self.treasure_list = []
        self.last_time = 0
        self.sec_last_time = 0

    def compare_func1(self,crew1:CrewMate,crew2:CrewMate):
        return crew1.load < crew2.load

    def add_treasure(self, treasure:Treasure):
        '''
            Arguments:
                treasure : Treasure : The treasure to be added to the treasury
            Returns:
                None
            Description:
                Adds the treasure to the treasury
            Time Complexity:
                O(log(m) + log(n)) where
                    m : Number of Crew Mates
                    n : Number of Treasures
        '''
        self.sec_last_time = self.last_time
        self.last_time = treasure.arrival_time
        time_diff = self.last_time - self.sec_last_time
        for i in self.crew_heap.init_array:
            i.load -= time_diff
            if i.load < 0 : i.load = 0
        self.treasure_list.append(treasure)
        temp = self.crew_heap.extract()
        temp.add_treasure_in_crew(treasure)
        self.crew_heap.insert(temp)

    def get_completion_time(self):
        '''
            Arguments:
                None
            Returns:
                List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
            Description:
                Returns all the treasure after processing them
            Time Complexity:
                O(n(log(m) + log(n))) where
                    m : Number of Crew Mates
                    n : Number of Treasures
        '''
        for j in self.crew_heap.init_array :
            j.just_completion_time()
        return self.treasure_list

# #################   TESTING #################
# print("_"*20,"start testing","_"*20)
#
# # Initialize with 3 crew members
# straw = StrawHatTreasury(3)
#
# # 10 treasures with some having the same arrival time (collisions)
# treasure1 = Treasure(1001, 5, 1)  # Arrives at time 1
# straw.add_treasure(treasure1)
# print("load-", [i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# treasure2 = Treasure(1002, 4, 2)  # Arrives at time 2
# straw.add_treasure(treasure2)
# print("load-", [i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# treasure3 = Treasure(1003, 6, 3)  # Arrives at time 3
# straw.add_treasure(treasure3)
# print("load-", [i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# # Collision at time 4: 3 treasures arrive at the same time
# treasure4 = Treasure(1004, 7, 4)  # Arrives at time 4
# straw.add_treasure(treasure4)
# print("load-", [i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# # Additional treasures arriving in sequence
# treasure7 = Treasure(1007, 3, 5)  # Arrives at time 5
# straw.add_treasure(treasure7)
# print("load-", [i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# treasure8 = Treasure(1008, 9, 6)  # Arrives at time 6
# straw.add_treasure(treasure8)
# print("load-", [i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# treasure9 = Treasure(1009, 4, 7)  # Arrives at time 7
# straw.add_treasure(treasure9)
# print("load-", [i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# treasure10 = Treasure(1010, 1, 8)  # Arrives at time 8
# straw.add_treasure(treasure10)
# print("load-", [i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
#
#
# #################   TESTING #################
# print("_"*20,"start testing","_"*20)
#
# straw = StrawHatTreasury(3)
# treasure1 = Treasure(1001,8,1)
# straw.add_treasure(treasure1)
# print("load-",[i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# treasure2 = Treasure(1002,7,2)
# straw.add_treasure(treasure2)
# print("load-",[i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# treasure3 = Treasure(1003,4,4)
# straw.add_treasure(treasure3)
# print("load-",[i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
#
# treasure4 = Treasure(1004,1,5)
# straw.add_treasure(treasure4)
# print("load-",[i.load for i in straw.crew_heap.init_array])
# straw.get_completion_time()
# print("-"*50)
