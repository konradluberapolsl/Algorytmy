class Queue:
    def __init__(self, capacity):
        self.Queue = [None] * capacity
        self.capacity = int(capacity)
        self.end = 0
        self.front = 0

    def __str__(self):
        if self.isempty(): return "Kolejka jest pusta"
        else: return str(list(reversed(self.Queue)))

    def isempty(self):
        return self.size() == 0

    def isfull(self):
        #return self.size() == self.capacity
        return None not in self.Queue


    def size(self):
        try:
            x = self.Queue.index(None)
        except ValueError:
            return self.capacity
        return  x


    def peek(self):
        if self.isempty(): return None
        else: return self.Queue[0]

    def enqueue(self, element):
        if self.isfull():
            print("Kolejka jest przepełniona, zosatnie nadpisana")
            # self.end = (self.end + 1) % self.capacity + nowe pole size=0 żeby działało
            #self.front = (self.front + 1) % self.capacity
        self.Queue.pop(self.end)
        self.Queue.insert(self.end,element)
        self.end = (self.end + 1) % self.capacity


    def dequeue(self):
        if self.isempty(): return None
        else :
            print("Element: "+ str(self.Queue[0]) + " opuscił kolejke")
            self.Queue.pop(0)
            self.Queue.append(None)
            #self.end = (self.end + 1) % self.capacity



    def find(self, element):
        #index(elemnet) - zwraca tylko pierwszy napotkany
        if element in self.Queue:
            indexes=[]
            for i in range(len(self.Queue)):
                if self.Queue[i] == element: indexes.append(i)
            return  indexes
        else: return None


q = Queue(3)
print(q)
q.enqueue(1)
print(q)
q.enqueue(3)
print(q)
q.enqueue(5)
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.enqueue(7)
print(q)
q.dequeue()
print(q)
# print("Przejście drugie:")
# q.enqueue(7)
# print(q)
# q.enqueue(-12)
# print(q)
# q.enqueue(15)
# print(q)
# print("Przejście trzecie:")
# q.enqueue(18)
# print(q)
# q.dequeue()
# print(q)
# q.dequeue()
# print(q)
# q.dequeue()
# print(q)
# q.enqueue(17)
# print(q)
# q.enqueue(1)
# print(q)
# q.enqueue(3)
# print(q)
# q.enqueue(5)
# print(q)
