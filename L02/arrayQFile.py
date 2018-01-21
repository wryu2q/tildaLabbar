from array import array


class ArrayQ:
    '''' An array implementation of a queue'''
    def __init__(self):
        self.__queue = array('i', [])

    def enqueue(self, number):
        ''' Adds to the end of the queue, which is the first place in the array'''
        self.__queue.insert(0, number)

    def dequeue(self):
        ''' Returns  and removes from queue the first item of the queue, which is the last item of the array'''
        return self.__queue.pop()


def test():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if x == 1 and y == 2:
        print("Fungerar")
    else:
        print("Något är fel. 1 och 2 förväntades men vi fick", x, y)


if __name__ == "__main__":
    test()
