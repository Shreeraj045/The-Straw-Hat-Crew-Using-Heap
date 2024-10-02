'''
    This file contains the class definition for the StrawHat class.
'''
from crewmate import CrewMate
from heap import Heap
from treasure import Treasure

class StrawHatTreasury:
    def __init__(self, m):
        self.number = m
        self.last_time = 0
        self.crew_heap = Heap(self.compare_func1,[CrewMate() for i in range(m)])
        self.treasure_list = []

    def compare_func1(self,crew1:CrewMate,crew2:CrewMate):
        return crew1.curr_load(self.last_time) < crew2.curr_load(self.last_time)

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
        self.treasure_list.append(treasure)
        self.last_time = treasure.arrival_time
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
        return sorted(self.treasure_list, key=lambda x: x.id)