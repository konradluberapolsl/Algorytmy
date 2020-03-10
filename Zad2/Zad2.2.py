class PriorityQueue:
    def __init__(self):
        self.PQueue = []

    def __str__(self):
        if self.isEmpty():
            return "Kolejka jest pusta"
        else:
            return str(self.PQueue)

    def isEmpty(self):
        if len(self.PQueue) == 0:
            return True
        else:
            return False

    def Front(self):
        return self.PQueue[0]

    def Size(self):
        return len(self.PQueue)

    def Push(self, end, prio):
        # def myFunc(element):
        #     return element[1]
        # self.PQueue.append((end, prio))
        # if not self.isEmpty():
        #     self.PQueue.sort(reverse=True, key=myFunc)
        if not self.isEmpty():
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
        else:
            self.PQueue.append((end, prio))

    def Pop(self):
        if self.isEmpty():
            return print("Kolejka jest pusta")
        else:
            self.PQueue.pop(len(self.PQueue)-1)


q = PriorityQueue()
q.Push(1, 10)
q.Push(3, 6)
q.Push(2, 2)
q.Push(20,0)
q.Push(5,120)
q.Push(3,-1)
q.Push(2,0)
q.Push(2,0)

print(q)
q.Pop()
q.Pop()

print(q)