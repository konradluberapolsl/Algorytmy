class Queue:
    def __init__(self):
        self.Queue = []

    def __str__(self):
        if self.isEmpty(): return "Kolejka jest pusta"
        else: return str(self.Queue)

    def isEmpty(self):
        if len(self.Queue) == 0: return True
        else: return False

    def Size(self):
        return len(self.Queue)

    def Front(self):
        return self.Queue[0]

    def Push(self, end):
        self.Queue.append(end)

    def Pop(self):
        if self.isEmpty(): return print("Kolejka jest pusta")
        else : self.Queue.pop(0)


q = Queue()
q.Push(1)
q.Push(2)
q.Push(3)
print(q)
