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
        self.treasure_heap = Heap(self._compare_func())
        self.last_time = 0
        self.sec_last_time = 0


    # Add more methods if required

    def _compare_func(self,tresure1:Treasure,tresure2:Treasure):
        # return tresure1.size < tresure2.size
        p1 = tresure1.priority()
        p2 = tresure2.priority()
        if p1 != p2:
            return p1 < p2
        else:
            return tresure1.id < tresure2.id

    def add_treasure_in_crew(self,treasure:Treasure):
        self.load += treasure.size

        self.sec_last_time = self.last_time
        self.last_time = treasure.arrival_time
        self.change_size_in_time()

        self.treasure_heap.insert(treasure)

    def change_size_in_time(self):
        time = self.sec_last_time -self.last_time
        c = self.sec_last_time
        while time > 0:
            temp = self.treasure_heap.top()
            if time >= temp.size:
                time -= temp.size
                c += temp.size
                temp.size = 0
                self.treasure_heap.extract()
                temp.completion_time = c
            else:
                temp.size -= time
                time = 0
                c = time2





