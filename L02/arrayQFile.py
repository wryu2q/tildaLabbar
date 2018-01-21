from array import array
class ArrayQ:
    def __init__(self):
        self.__queue = array('i', [])

    def enqueue(self, number):
        self.__queue.insert(0, number)

    def dequeue(self):
        return self.__queue.pop()

def test():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("Fungerar")
    else:
        print("Något är fel. 1 och 2 förväntades men vi fick", x, y)

test()