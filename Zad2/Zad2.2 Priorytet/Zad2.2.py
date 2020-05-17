class PriorityQueue:
    def __init__(self, capacity):
        self.PriorityQueue = []
        self.capacity = int(capacity)

    def __str__(self):
        if self.is_empty():
            return "kolejka jest pusta"
        else:
            return str(self.PriorityQueue)

    def size_of_queue(self):
        return len(self.PriorityQueue)

    def is_empty(self):
        if self.size_of_queue() == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.size_of_queue() == self.capacity:
            return True
        else:
            return False

    # dodaje nowy element w zależności od priorytetu
    def push_element(self, item, prio):
        if not self.is_full():
            if not self.is_empty():
                for i in range(self.size_of_queue()):
                    if prio > self.PriorityQueue[i][1]:
                        self.PriorityQueue.insert(i, (item, prio))
                        break
                    elif prio < self.PriorityQueue[self.size_of_queue() - 1][1]:
                        self.PriorityQueue.append((item, prio))
            else:
                self.PriorityQueue.append((item, prio))
        else:
            print("kolejka jest pełna")

    # usuwa pierwszy element
    def pop_element(self):
        if not self.is_empty():
            self.PriorityQueue.pop(0)
        else:
            print("kolejka jest pusta")


kolejka = PriorityQueue(5)
kolejka.push_element("el1", 1)
print(kolejka)
kolejka.push_element("el2", 3)
print(kolejka)
kolejka.push_element("el3", 2)
print(kolejka)
kolejka.push_element("el4", 0)
print(kolejka)
kolejka.push_element("el5", 3)
print(kolejka)
kolejka.push_element("el6", 1)
