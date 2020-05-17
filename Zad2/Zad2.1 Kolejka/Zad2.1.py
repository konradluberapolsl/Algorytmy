class Queue:
    def __init__(self, capacity):
        self.Queue = []
        self.capacity = int(capacity)

    def __str__(self):
        if self.is_empty():
            return "kolejka jest pusta"
        else:
            return str(self.Queue)

    def size_of_queue(self):
        return len(self.Queue)

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

    # dodaje nowy element na końcu
    def push_element(self, item):
        if not self.is_full():
            self.Queue.append(item)
        else:
            print("kolejka jest pełna")

    # usuwa pierwszy element
    def pop_element(self):
        if not self.is_empty():
            self.Queue.pop(0)
        else:
            print("kolejka jest pusta")


kolejka = Queue(5)

kolejka.push_element(1)
print(kolejka)
kolejka.push_element(2)
print(kolejka)
kolejka.push_element(3)
print(kolejka)
kolejka.push_element(4)
print(kolejka)
kolejka.push_element(5)
print(kolejka)
kolejka.push_element(6)
kolejka.pop_element()
print(kolejka)
kolejka.pop_element()
print(kolejka)
kolejka.pop_element()
print(kolejka)
kolejka.pop_element()
print(kolejka)
kolejka.pop_element()
print(kolejka)
