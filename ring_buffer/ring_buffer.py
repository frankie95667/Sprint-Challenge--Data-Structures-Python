from singly_linked_list import LinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = None
        self.position = 0

    def append(self, item):
        if self.storage is not None:
            self.storage.add_to_pos(item, self.position)
        else:
            self.storage = LinkedList()
            self.storage.add_to_pos(item, self.position)
        self.position += 1
        if self.position == self.capacity:
            self.position = 0

    def get(self):
        arr = []
        if self.storage is not None:
            current = self.storage.head
            while current is not None:
                arr.append(current.get_value())
                current = current.get_next()
        return arr