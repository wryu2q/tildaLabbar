class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None


class LinkedQ:
    def __init__(self):
        self.__first = Node()
        self.__last = self.__first

    def enqueue(self, data):
        if self.__first.val == None:
            self.__first.val = data
        else:
            self.__last.next = Node(data)
            self.__last = self.__last.next

    def dequeue(self):
        try:
            toBeReturned = self.__first.val
        except AttributeError:
            raise IndexError("Queue is empty")
        try:
            self.__first = self.__first.next
        except AttributeError:
            pass
        return toBeReturned

def test():
    q = LinkedQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("Fungerar")
    else:
        print("Något är fel. 1 och 2 förväntades men vi fick", x, y)

if __name__ == "__main__":
    test()

