class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.length  = 0
        self.position = 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node
        self.length += 1
    
    def add_to_pos(self, value, pos):
        start = self.head
        current = start
        if pos == 0 and self.head is not None:
            self.head = Node(value, current.get_next())
        elif pos == 0 and self.head is None:
            self.head = Node(value, current)
        else:
            while pos > 1:
                current = current.get_next()
                pos -= 1
            if current.get_next() is not None:
                current.set_next(Node(value, current.get_next().get_next()))
            else:
                current.set_next(Node(value, current.get_next()))
            self.head = start

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prev = prev
        current = node
        while current is not None:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev
