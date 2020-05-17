
class SingleLinkedList:
    def __init__(self):
        self.capacity = capacity
        self.List = [None] *self.capacity
    def Push(self,item):
        if len(self.List)==0:
            self.List.append((item,))
