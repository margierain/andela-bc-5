import unittest

from mathx.super_sum import super_sum

class SuperSumTest(unittest.TestCase):

	def test_sum_two_numbers(self):
		result = super_sum(20, 20)
		self.assertEqual(result, 40)

	def test_four_numbers(self):
		result = super_sum(10,20,30,40)
		self.assertEqual(result, 100)

	def test_test_lists(self):
	    a = [10, 20, 30, 40]
	    b = [140, 60]
	    result = super_sum(a, b)
	    self.assertEqual(result,300)

	def test_four_lists(self):
	    a,b,c,d = [1, 2],[3, 4], [5, 6], [7, 8]
	    result = super_sum(a, b, c, d)
	    self.assertEqual(result, 36)  


	#def test_large_input(self):
	#pass	