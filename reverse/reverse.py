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

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

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
        # pass
        # # check if the ll is empty
        if self.head is None:
            return None
        # check if there is only one node / if recursion reached the tail
        if node.get_next() is None:
            self.head = node
        # otherwise more than one node
        if node.get_next():
            # while there is a next child, repeat the process with recursion on the next child
            self.reverse_list(node.get_next(), node)
        # node's next is its previous 
        node.set_next(prev)
            
        

ll = LinkedList()
ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
print('original head',ll.head.value)
ll.reverse_list(ll.head, None)
print('new head',ll.head.value)
print(ll.head.get_next().value)
