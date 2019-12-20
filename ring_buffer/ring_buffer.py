from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == self.storage.length:
            # if current is the tail, then remove from head, add item to head, and point current to head
            if self.current == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head

            # else insert after current
            # change current to currents next
            # delete what is after the new current
            else:
                self.current.insert_after(item)
                self.storage.length += 1
                self.current = self.current.next
                self.storage.delete(self.current.next)
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head

        # TODO: Your code here
        if self.storage.length == 1:
            list_buffer_contents.append(self.storage.head.value)
        elif self.storage.length > 1:
            while current.next:
                list_buffer_contents.append(current.value)
                current = current.next
            list_buffer_contents.append(current.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1
        

    def get(self):
        return [value for value in self.storage if value]
