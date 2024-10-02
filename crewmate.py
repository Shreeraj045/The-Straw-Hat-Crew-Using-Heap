# Python file to implement the class CrewMate
from heap import Heap
from treasure import Treasure
class CrewMate:
    def __init__(self):
        self.load = 0
        self.treasure_heap = Heap(self._compare_func,[])
        self.last_time = 0
        self.sec_last_time = 0
    def _compare_func(self,tresure1:Treasure,tresure2:Treasure):
        p1 = tresure1.priority()
        p2 = tresure2.priority()
        if p1 != p2:
            return p1 < p2
        else:
            return tresure1.id < tresure2.id

    def add_treasure_in_crew(self,treasure:Treasure):
        # print(0,end='')
        self.sec_last_time = self.last_time
        self.last_time = treasure.arrival_time

        self.change_size_in_time()
        if self.treasure_heap.top() == None:
            self.load = treasure.arrival_time

        self.load += treasure.size
        self.treasure_heap.insert(treasure)

    def change_size_in_time(self):
        time = self.last_time - self.sec_last_time
        c = self.sec_last_time
        if  self.sec_last_time == 0:
            return
        while time > 0 and self.treasure_heap.top() != None:
            top_treasure = self.treasure_heap.top()
            if time >= top_treasure.size:
                time -= top_treasure.size
                c += self.treasure_heap.top().size
                top_treasure.completion_time = c
                self.treasure_heap.extract()
            else:
                self.treasure_heap.top().size -= time
                time = 0
                c = self.last_time

    def just_completion_time(self):
        array = self.treasure_heap.copy_heap()
        c = self.last_time
        while self.treasure_heap.top() != None :
            c += self.treasure_heap.top().size
            self.treasure_heap.top().completion_time = c
            self.treasure_heap.extract()
        for i in array:
            self.treasure_heap.insert(i)

        # array = self.treasure_heap.init_array
        # print(array)
        # curr_time = self.last_time
        # for treasure in array :
        #     # print(0,end='')
        #     curr_time += treasure.size
        #     treasure.completion_time = curr_time

        # curr_time = self.last_time
        #
        # # Process the treasures directly from the heap
        # while self.treasure_heap.top() is not None:
        #     top_treasure = self.treasure_heap.top()
        #     curr_time += top_treasure.size
        #     top_treasure.completion_time = curr_time
        #     self.treasure_heap.extract()  #

    def curr_load(self,time):
        curr_load = self.load - time
        if curr_load <0 :curr_load = 0
        return curr_load
