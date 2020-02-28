from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == self.current:
            max_value = self.storage.get_max()
            if max_value == self.storage.tail.value:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
            elif max_value == self.storage.tail.prev.value:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
            elif max_value == self.storage.head.value:
                self.storage.head.next.delete()
                self.storage.head.insert_after(item)
            else:
                current_node = self.storage.head.next
                while current_node.value < max_value:
                    current_node = current_node.next
                current_node.next.delete()
                current_node.insert_after(item)

        else:
            self.current += 1
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        def add_to_list(node):
            if not node:
                return
            else:
                list_buffer_contents.append(node.value)
                add_to_list(node.next)

        add_to_list(self.storage.head)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        if self.capacity == self.current:
            max_value = self.storage[0]
            max_index = 0
            for index, val in enumerate(self.storage):
                if val > max_value:
                    max_value = val
                    max_index = index
            if max_value == self.storage[-1]:
                self.storage[0] = item
            elif max_value == self.storage[-2]:
                self.storage[-1] = item
            else:
                self.storage[max_index + 1] = item

        else:
            self.current += 1
            index = 0
            for el in self.storage:
                if el != None:
                    index += 1
            self.storage[index] = item

    def get(self):
        container = []
        for i in range(len(self.storage)):
            if self.storage[i] != None:
                container.append(self.storage[i])
        return container


# ring = ArrayRingBuffer(5)
# ring.append('a')
# ring.append('b')
# ring.append('c')
# ring.append('d')
# ring.append('e')
# ring.append('f')
# ring.append('g')
# print(len(ring.storage), "<<<< len")
# print(ring.get(), "<<<< container")
# print(ring.storage, "<<<< ring.storage")
