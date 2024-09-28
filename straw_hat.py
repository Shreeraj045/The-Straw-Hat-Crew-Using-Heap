'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
from custom import Inter_treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        # Write your code here


        self.number = m
        self.crew_heap = Heap(self.compare_func1())
        self.treasure_list = []
        self.last_time = 0
        self.sec_last_time = 0


    def compare_func1(self,crew1:CrewMate,crew2:CrewMate):
        return crew1.load < crew2.load

    def add_treasure(self, treasure):
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
        custom_treasure = treasure
        time_diff = self.last_time - self.sec_last_time
        print(time_diff)
        for i in self.crew_heap.init_array:
            i.load -= time_diff
            if i.load <0 : i.load = 0
        self.treasure_list.append(custom_treasure)
        temp = self.crew_heap.extract()
        temp.add_treasure_in_crew(custom_treasure)
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
        # Write your code here
        for j in self.crew_heap.init_array :
            i.just_completion_time()

        for i in self.treasure_list:
            print(i)
    
    # You can add more methods if required

#################   TESTING #################
print("_"*20,"start testing","_"*20)

