# Python file to implement the class CrewMate
from heap import Heap
from treasure import Treasure
class CrewMate:
    # Class to implement a crewmate
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''

        
        # Write your code here
        self.load = 0
        self.treasure_heap = Heap(self._compare_func)


    # Add more methods if required

    def _compare_func(self,tresure1:Treasure,tresure2:Treasure):
        # return tresure1.size < tresure2.size
        return (tresure1.arrival_time + tresure1.size) < ( tresure2.arrival_time + tresure2.size )

    def add_treasure_in_crew(self,treasure:Treasure):
        self.load += treasure.size
        self.treasure_heap.insert(treasure)

