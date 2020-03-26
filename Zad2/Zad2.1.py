class Queue:
    def __init__(self, capacity):
        self.Queue = []
        self.capacity = int(capacity)

    def __str__(self):
        if self.isempty(): return "Kolejka jest pusta"
        else: return str(list(reversed(self.Queue)))

    def isempty(self):
        if len(self.Queue) == 0: return True
        else: return False

    def size(self):
        return len(self.Queue)

    def peek(self):
        if self.isempty(): return None
        else: return self.Queue[0]

    def enqueue(self, end):
        if len(self.Queue) == self.capacity:
            print("Kolejka jest przepełniona, zostanie powiększona")
        self.Queue.append(end)

    def dequeue(self):
        if self.isempty(): return None
        else :
            print("Element: "+ str(self.Queue[0]) + " opuscił kolejke")
            self.Queue.pop(0)

    def find(self, element):
        #index(elemnet) - zwraca tylko pierwszy napotkany
        if element in self.Queue:
            indexes=[]
            for i in range(len(self.Queue)):
                if self.Queue[i] == element: indexes.append(i)
            return  indexes
        else: return None


q = Queue(3)
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
q.enqueue(5)
q.enqueue("qweqeq")
print(q)
q.dequeue()
print(q.size())
print(q.find(5))
print(q.find(6))
