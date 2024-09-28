# Python file to implement the class CrewMate
from heap import Heap
from treasure import Treasure
from custom import Inter_treasure
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
        self.treasure_heap = Heap(self._compare_func,[])
        self.last_time = 0
        self.sec_last_time = 0


    # Add more methods if required

    def _compare_func(self,tresure1:Inter_treasure,tresure2:Inter_treasure):
        # return tresure1.size < tresure2.size
        p1 = tresure1.priority()
        p2 = tresure2.priority()
        if p1 != p2:
            return p1 < p2
        else:
            return tresure1.id < tresure2.id

    def add_treasure_in_crew(self,treasure:Treasure):
        treasure_inter = Inter_treasure(treasure)
        self.load += treasure_inter.size

        self.sec_last_time = self.last_time
        self.last_time = treasure_inter.arrival_time

        self.change_size_in_time()

        self.treasure_heap.insert(treasure_inter)

    def change_size_in_time(self):
        time = self.last_time -self.sec_last_time
        c = self.sec_last_time
        if self.sec_last_time != 0 :
            while time > 0:
                print(time)
                if self.treasure_heap.top() != None:
                    if time >= self.treasure_heap.top().size:
                        time -= self.treasure_heap.top().size
                        c += self.treasure_heap.top().size
                        self.treasure_heap.top().size = 0
                        self.treasure_heap.top().set_completion_time(c)
                        self.treasure_heap.extract()
                    else:
                        self.treasure_heap.top().size -= time
                        time = 0
                        c = self.last_time
                else:
                    break




##########   TESTING ############

crew = CrewMate()

print("load-",crew.load)
print("heap-",end='')
lis = crew.treasure_heap.init_array
print([i.size for i in lis])
print("last_time -",crew.last_time)
print("secomd_last_time - ",crew.sec_last_time)
print("-"*50)

tresure1 = Treasure(1001,4,4)
crew.add_treasure_in_crew(tresure1)

print("load-",crew.load)
print("heap-",end='')
lis = crew.treasure_heap.init_array
print([i.size for i in lis])
print("last_time -",crew.last_time)
print("secomd_last_time - ",crew.sec_last_time)
print("-"*50)

tresure2 = Treasure(1003,1,5)

crew.add_treasure_in_crew(tresure2)

print("load-",crew.load)
print("heap-",end='')
lis = crew.treasure_heap.init_array
print([i.size for i in lis])
print("last_time -",crew.last_time)
print("secomd_last_time - ",crew.sec_last_time)
print("-"*50)

tresure3 = Treasure(1006,4,14)
crew.add_treasure_in_crew(tresure3)

print("load-",crew.load)
lis = crew.treasure_heap.init_array
print("curr_heap - ",[i.size for i in lis])

print("last_time -",crew.last_time)
print("secomd_last_time - ",crew.sec_last_time)
print("-"*50)

print(tresure1.completion_time)
print(tresure2.completion_time)
print(tresure3.completion_time)







