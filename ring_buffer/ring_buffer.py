class RingBuffer:
    def __init__(self, capacity):
        # pass
        self.capacity = capacity
        self.buffer = []
        self.free_index = 0

    def append(self, item): # FIFO -- First item in is the first item we kick out
        # pass
        
        if len(self.buffer) < self.capacity:
            # insert item at free index
            self.buffer.append(item)

        elif len(self.buffer) == self.capacity:
            if self.free_index == self.capacity:
                self.free_index = 0
            self.buffer.pop(self.free_index)
            self.buffer.insert(self.free_index, item)
            self.free_index += 1
            
        # print(self.free_index)
        # return self.buffer
        
    def get(self):
        # pass
        return self.buffer


# buffer = RingBuffer(3)
# print(buffer.append(1))
# print(buffer.append(2))
# print(buffer.append(3))
# print(buffer.append(4))
# print(buffer.append(5))
# print(buffer.append(6))
# print(buffer.append(7))