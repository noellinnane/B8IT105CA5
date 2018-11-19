import unittest

from new_calc import sum1, sum2, sub1, sub2, mult1, div1, div2, sq1, sqr2, sqr3

class CalcTest(unittest.TestCase):
    
       
    def testSum1(self):
        self.assertEqual(10, sum1([1,2,3,4]))
        self.assertEqual(20, sum1([5,5,5,5]))
        
    def testSum2(self):
        self.assertEqual([2,2], sum2([1,1],[1,1]))
        
    def testSub1(self):
        self.assertEqual(1, sub1([2,1]))
        self.assertEqual(0, sub1([1,1]))
        self.assertEqual(-1, sub1([0,1]))
        
    def testSub2(self):
        self.assertEqual([1,1], sub2([2,2],[1,1]))
        self.assertEqual([-1,0], sub2([1,1],[2,1]))
        
    def testMult1(self):
        self.assertEqual(25, mult1([5,5]))
        
    def testMult2(self):
        self.assertEqual([25,25], mult2([5,5],[5,5]))
        
    def testDiv1(self):
        self.assertEqual(2, div1([2,1]))
        
    def testDiv2(self):
        self.assertEqual([2,2], div2([2,2],[1,1]))
        
    def testSq1(self):
        self.assertEqual([1,4,9,16,25], sq1([1,2,3,4,5]))
        
    def testSq2(self):
        self.assertEqual([0, 1, 4, 9, 16, 25, 36, 49, 64], sqr2(9))
        
    def testSqr3(self):
        a = sqr3(9)
        self.assertEqual(0, next(a))
        self.assertEqual(1, next(a))
        self.assertEqual(4, next(a))
        self.assertEqual(9, next(a))
        self.assertEqual(16, next(a))
        self.assertEqual(25, next(a))
        self.assertEqual(36, next(a))
        self.assertEqual(49, next(a))
        self.assertEqual(64, next(a))
        
        
        
unittest.main()        