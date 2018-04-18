import unittest
import random
from cuppgift import findKthBest, generateList
from statistik import Statistik


class SyntaxTest(unittest.TestCase):
    def test0(self):
        for k in range(0, 4):
            self.assertEqual(findKthBest(k, [0, 1, 2, 3], 0, 3, Statistik()), k)

    def test1(self):
        for k in range(0, 3):
            self.assertEqual(findKthBest(k, [0, 1, 0, 0], 0, 3, Statistik()), 0)
            
    def test2(self):
        N = 3
        data = list(range(0, N))
        for i in range(0, 200):
            random.shuffle(data)
            #data = generateList(N, 1)
            k = random.randint(0, N-1)
            self.assertEqual(findKthBest(k, data, 0, N-1, Statistik()), k)


if __name__ == '__main__':
    unittest.main()
