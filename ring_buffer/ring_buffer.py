from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the buffer is at capacity
        if self.storage.length == self.capacity:
            # if current is at the tail, that means the item must be appended to the head
            if self.current == self.storage.tail:
                # remove the current head
                self.storage.remove_from_head()
                # add item to head
                self.storage.add_to_head(item)
                # set current equal to the new head
                self.current = self.storage.head
            # else, current is somewhere other than the tail
            else:
                # insert item just after current
                self.current.insert_after(item)
                # update length because insert_after does not
                self.storage.length += 1
                # update current
                self.current = self.current.next
                # delete item that is just after current aka the oldest item
                self.storage.delete(self.current.next)
        # otherwise, if the buffer is not at capacity, aka below capacity
        else:
            # add item to tail of buffer
            self.storage.add_to_tail(item)
            # update current to point to tail
            self.current = self.storage.tail
    
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # create a variable - item - to start by pointing at head
        item = self.storage.head
        # while item is not None
        while item is not None:
            # append item to the list buffer content provided
            list_buffer_contents.append(item.value)
            # update item to the next in list
            item = item.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0 # represents the index of the current item in storage
        self.storage = [None] * capacity

    def append(self, item):
        # append item to storage at current index
        self.storage[self.current] = item
        # update current
        # if at the end of the storage, current is updated to index 0
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        # use a list comprehension to add each item from the ring buffer
        return [item for item in self.storage if item]
    