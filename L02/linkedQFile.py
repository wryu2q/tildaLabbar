class Node:
    ''' Creates a node for a linked list, containing value and nex attributes'''
    def __init__(self, data=None):
        self.val = data
        self.next = None


class LinkedQ:
    ''' A linked list implementation of a queue'''
    def __init__(self):
        self.__first = Node()
        self.__last = self.__first

    def enqueue(self, data):
        ''' Adds to the end of the queue, which is the end of the linked list'''
        try:
            if self.__first.val is None:
                self.__first.val = data
            else:
                self.__last.next = Node(data)
                self.__last = self.__last.next
        except AttributeError:
            self.__first = Node(data)

    def dequeue(self):
        ''' Returns the first item of the queue, which is the first item of the linked list'''
        try:
            to_be_returned = self.__first.val
        except AttributeError:
            self.__first = Node()
            raise IndexError("Queue is empty")

        try:
            self.__first = self.__first.next
        except AttributeError:
            pass
        return to_be_returned

    def isEmpty(self):
        ''' Returns True if queue is empty '''
        try:
            if self.__first.val is None:
                return True
        except AttributeError:
            return True
        return False
    
def test():
    q = LinkedQ()
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    print(q.isEmpty())
    y = q.dequeue()
    print(q.isEmpty())
    q.enqueue(3)
    print(q.dequeue())
    if x == 1 and y == 2:
        print("Fungerar")
    else:
        print("Något är fel. 1 och 2 förväntades men vi fick", x, y)


if __name__ == "__main__":
    test()
