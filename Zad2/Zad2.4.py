# Ponieważ w pythonie nie ma wskaźników to musiałem użyć implementacji wskaźnikowej plus nie ma tablc takich jak np w C# więc postanowiłem ograniczyć rozmiar listy pythona tak aby działa jak tablica

class SingleLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.List = [None] *self.capacity
    def Push(self,item):
        if len(self.List)==0:
            self.List.append((item,))
