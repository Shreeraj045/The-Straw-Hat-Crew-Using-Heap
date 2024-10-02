from straw_hat import *
from heap import *
from treasure import *
import random


random.seed(42)


def progress_bar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    total = len(iterable)
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    printProgressBar(0)
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    print()


class Chest:
    def __init__(self, chest_id, arrival_time, original_size):
        self.chest_id = chest_id
        self.arrival_time = arrival_time
        self.original_size = original_size
        self.remaining_size = original_size
        self.waiting_time = 0
        self.processed = 0


class Worker:
    def __init__(self, worker_id):
        self.worker_id = worker_id
        self.chests = []
        self.current_chest = None


class Manual:
    def __init__(self, chests, n):
        self.chests = [Chest(*chest) for chest in chests]
        self.workers = [Worker(i) for i in range(n)]
        self.time = 0
        self.completion_times = {}
        for chest in self.chests:
            self.completion_times[chest.chest_id] = 0
            if chest.arrival_time == 0:
                self.workers[0].chests.append(chest)

    def tick(self):
        self.time += 1
        for worker in self.workers:
            for chest in worker.chests:
                chest.waiting_time += 1
        for chest in self.chests:
            if chest.arrival_time == self.time:
                min_load = sum([sum([chest.remaining_size for chest in worker.chests]) for worker in self.workers])
                best_worker = None
                for worker in self.workers:
                    load = sum([chest.remaining_size for chest in worker.chests])
                    if load <= min_load:
                        min_load = load
                        best_worker = worker
                best_worker.chests.append(chest)

        for worker in self.workers:
            if worker.current_chest:
                worker.current_chest.remaining_size -= 1
                worker.current_chest.processed += 1
                if worker.current_chest.remaining_size == 0:
                    worker.chests.remove(worker.current_chest)
                    self.completion_times[worker.current_chest.chest_id] = self.time
                    worker.current_chest = None
            if worker.chests:
                max_cri = worker.chests[0].waiting_time - worker.chests[0].remaining_size
                best_chest = None
                for chest in worker.chests:
                    cri = chest.waiting_time - chest.remaining_size
                    if cri >= max_cri:
                        max_cri = cri
                        best_chest = chest
                worker.current_chest = best_chest

    def print_current_status(self):
        print(f"Time: {self.time}")
        for worker in self.workers:
            print(f"Worker {worker.worker_id}: ", end="")
            if worker.current_chest:
                print(f"Processing Chest {worker.current_chest.chest_id} with {worker.current_chest.remaining_size} units left")
            else:
                print("Idle")
        print()

    def get_completion_time(self):
        return sorted([(chest_id, time) for chest_id, time in self.completion_times.items()], key=lambda x: x[0])


class StupidHeap:
    def __init__(self, comparison_function, init_array):
        self.comparison_function = comparison_function
        self.heap = sorted(init_array, key=comparison_function)

    def insert(self, item):
        self.heap.append(item)
        self.heap = sorted(self.heap, key=self.comparison_function)

    def extract(self):
        return self.heap.pop(0)

    def top(self):
        return self.heap[0]

    def empty(self):
        return len(self.heap) == 0

# manual = Manual([(1, 1, 8), (2, 2, 7), (3, 4, 4), (4, 5, 1)], 3)
# for i in range(9):
#     manual.tick()
# print(manual.get_completion_time())

# treasury = StrawHatTreasury(3)
# treasury.add_treasure(Treasure(1, 8, 1))
# treasury.add_treasure(Treasure(2, 7, 2))
# treasury.add_treasure(Treasure(3, 4, 4))
# treasury.add_treasure(Treasure(4, 1, 5))
# treasury.print_completion_times(treasury.get_completion_time())


def main(n=10**3, m=20):
    format_len = 25
    workers = m
    print("[+] Welcome to Ani's Testcase (V1.0), this will be a comprehensive testcase and will automatically check for correctness.\n[*] Do not rely on this for time complexity testing, it is not accurate.\n[!] Unlike last time, this testcase will strictly adhere to possible operations, any errors indicate an issue in your code.\n[!] If you think that there is an error in the testcase or if I'm missing something, dm me whatsapp pr")
    stupid_heap = StupidHeap(lambda x: x, [1, 2, 3, 4, 5])
    test_heap = Heap(lambda x, y: x < y, [1, 2, 3, 4, 5])
    for i in progress_bar(range(n), "Random Heap Operations".ljust(format_len)):
        op = random.randint(0, 100)
        if op <= 75:
            val = random.randint(0, 10000)
            if val not in stupid_heap.heap:
                stupid_heap.insert(val)
                test_heap.insert(val)
            stupid_top = stupid_heap.top()
            test_top = test_heap.top()
            if stupid_top != test_top:
                print(f"\n[!] Error while checking min value in heap after adding {val}, expected {stupid_top}, received {test_top}")
                exit(1)
        else:
            if not stupid_heap.empty():
                stupid_top = stupid_heap.top()
                test_top = test_heap.top()
                if stupid_top != test_top:
                    print(f"\n[!] Error while checking min value in heap, expected {stupid_top}, received {test_top}")
                    exit(1)
                stupid_pop = stupid_heap.extract()
                test_pop = test_heap.extract()
                if stupid_pop != test_pop:
                    print(f"\n[!] Pretty Major Error in your heap, running the top() function gave the correct value ({test_top}) but running the pop() function gave the value ({stupid_pop})")
                    exit(1)
                stupid_top = stupid_heap.top()
                test_top = test_heap.top()
                if stupid_top != test_top:
                    print(f"\n[!] Error while checking min value in heap after removing {test_pop}, expected {stupid_top}, received {test_top}")
                    exit(1)
    to_delete = stupid_heap.heap.copy()
    random.shuffle(to_delete)
    for i in progress_bar(to_delete, "Clearing Heap".ljust(format_len)):
        if not stupid_heap.empty():
            stupid_top = stupid_heap.top()
            test_top = test_heap.top()
            if stupid_top != test_top:
                print(f"\n[!] Error while checking min value in heap, expected {stupid_top}, received {test_top}")
                exit(1)
            stupid_pop = stupid_heap.extract()
            test_pop = test_heap.extract()
            if stupid_pop != test_pop:
                print(f"\n[!] Pretty Major Error in your heap, running the top() function gave the correct value ({test_top}) but running the pop() function gave the value ({stupid_pop})")
                exit(1)
        else:
            if stupid_heap.empty() ^ test_heap.empty():
                print(f"\n[!] Error while checking if heap is empty, expected {stupid_heap.empty()}, received {test_heap.empty()}")
                exit(1)
    test_treasury = StrawHatTreasury(workers)
    last_added = 0
    added = []
    for i in progress_bar(range(n), "Adding Treasure".ljust(format_len)):
        arrival_time = last_added + random.randint(1, 20)
        size = random.randint(1, 40)
        test_treasury.add_treasure(Treasure(i, size, arrival_time))
        added.append((i, arrival_time, size))
        last_added = arrival_time
    stupid_treasury = Manual(added, workers)
    completion_times = test_treasury.get_completion_time().copy()
    completion_times_2 = test_treasury.get_completion_time().copy()
    max_time = max([chest[1] for chest in added])
    for i in progress_bar(range(max_time + 41), "Manually Running Time".ljust(format_len)):
        stupid_treasury.tick()
    stupid_completion_times = stupid_treasury.get_completion_time()
    for i in progress_bar(range(n+1), "Checking Completion Times"):
        if i == 0:
            for j in range(len(completion_times)):
                if not(completion_times[j].id == completion_times_2[j].id and completion_times[j].completion_time == completion_times_2[j].completion_time):
                    print(f"\n[!] Running get_completion_time() twice gave different results at index ({j}), this should not happen.")
                    exit(1)
        else:
            if completion_times[i - 1].completion_time != stupid_completion_times[i - 1][1]:
                print(f"\n[!] Error in completion times, expected {stupid_completion_times[i - 1]}, received {(completion_times[i - 1].id, completion_times[i - 1].arrival_time)}")
                exit(1)
    for i in progress_bar(range(n), "Adding Treasure".ljust(format_len)):
        arrival_time = last_added + random.randint(1, 20)
        size = random.randint(1, 40)
        test_treasury.add_treasure(Treasure(n+i, size, arrival_time))
        added.append((n+i, arrival_time, size))
        last_added = arrival_time
    stupid_treasury = Manual(added, workers)
    completion_times = test_treasury.get_completion_time().copy()
    completion_times_2 = test_treasury.get_completion_time().copy()
    max_time = max([chest[1] for chest in added])
    for i in progress_bar(range(max_time + 41), "Manually Running Time".ljust(format_len)):
        stupid_treasury.tick()
    stupid_completion_times = stupid_treasury.get_completion_time()
    for i in progress_bar(range(2*n + 1), "Checking Completion Times"):
        if i == 0:
            for j in range(len(completion_times)):
                if not (completion_times[j].id == completion_times_2[j].id and completion_times[j].completion_time == completion_times_2[j].completion_time):
                    print(f"\n[!] Running get_completion_time() twice gave different results at index ({j}), this should not happen.")
                    exit(1)
        else:
            if completion_times[i - 1].completion_time != stupid_completion_times[i - 1][1]:
                print(f"\n[!] Error in completion times, expected {stupid_completion_times[i - 1]}, received {(completion_times[i - 1].id, completion_times[i - 1].arrival_time)}")
                exit(1)
    last_added = 0
    added = []
    for i in progress_bar(range(n//3), "Deep Check".ljust(format_len)):
        workers = random.randint(m//2, 2*m)
        test_treasury = StrawHatTreasury(workers)
        arrival_time = last_added + random.randint(1, 20)
        size = random.randint(1, 40)
        test_treasury.add_treasure(Treasure(n+i, size, arrival_time))
        added.append((n+i, arrival_time, size))
        last_added = arrival_time
        stupid_treasury = Manual(added, workers)
        for j in added:
            test_treasury.add_treasure(Treasure(j[0], j[2], j[1]))
        completion_times = test_treasury.get_completion_time().copy()
        completion_times_2 = test_treasury.get_completion_time().copy()
        max_time = max([chest[1] for chest in added])
        for j in range(max_time + 41):
            stupid_treasury.tick()
        stupid_completion_times = stupid_treasury.get_completion_time()
        for j in range(i + 1):
            if j == 0:
                for k in range(len(completion_times)):
                    if not (completion_times[k].id == completion_times_2[k].id and completion_times[k].completion_time == completion_times_2[k].completion_time):
                        print(f"\n[!] Running get_completion_time() twice gave different results at index ({k}), this should not happen.")
                        exit(1)
            else:
                if completion_times[j - 1].completion_time != stupid_completion_times[j - 1][1]:
                    print(f"\n[!] Error in completion times, expected {stupid_completion_times[j - 1]}, received {(completion_times[j - 1].id, completion_times[j - 1].arrival_time)}")
                    exit(1)

    print("[+] All testcases passed!!")


if __name__ == "__main__":
    main()
