class PriorityQueue:
    def __init__(self, capacity):
        self.PQueue = []
        self.capacity = int(capacity)

    def __str__(self):
        if self.isempty(): return "Kolejka jest pusta"
        else: return str(self.PQueue)

    def isempty(self):
        if self.size() == 0: return True
        else: return False

    def peek(self):
        if self.isempty(): return None
        else: return self.PQueue[len(self.PQueue)-1]

    def size(self):
        return len(self.PQueue)

    def enqueue(self, end, prio):
        # def myFunc(element):
        #     return element[1]
        # self.PQueue.append((end, prio))
        # if not self.isEmpty():
        #     self.PQueue.sort(reverse=True, key=myFunc)
        if not self.isempty():
            if self.size() == self.capacity:
                print("Kolejka jest przepełniona, zostanie powiększona")
            for i in range(len(self.PQueue)):
                if self.PQueue[i][1] >prio:
                    self.PQueue.insert(i, (end, prio))
                    break
                elif self.PQueue[i][1] == prio:
                    if self.PQueue[i][0] > end:
                        self.PQueue.insert(i, (end, prio))
                        break
                    elif self.PQueue[i][0] == end:
                        print("Taki element już istnieje")
                        break
                elif i == len(self.PQueue)-1: self.PQueue.append((end, prio))
        else: self.PQueue.append((end, prio))

    def dequeue(self):
        if self.isempty(): return None
        else: self.PQueue.pop(len(self.PQueue)-1)