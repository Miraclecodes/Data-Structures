from SLLNode import *

class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL Object: head={}".format(self.head)

    def is_empty(self):
        return self.head is None

    def add_front(self, new_data):
        temp_node = SLLNode(new_data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def size(self):
        size = 0

        if self.head is None:
            return 0

        current = self.head

        while current is not None:
            size += 1
            current = current.get_next()

        return size
       

    def search(self, data):
        if self.head is None:
            return "Linked list is empty"
        
        current = self.head

        while current is not None:
            if current.get_data() == data:
                return True

            else:
                current = current.get_next()

        return False


    def remove(self, data):
        """Removes the first occurence of a node that 
		contains the data argument as its self.data variable.

		The time complexity is o(n)""" 

        if self.head is None:
            return "Linked list is empty"

        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True

            elif current.get_next() is None:
                return "Node not in list"

            else:
                previous = current
                current = current.get_next()
            
        if previous is None:
            self.head = current.get_next()

        else:
            previous.set_next(current.get_next())
            


