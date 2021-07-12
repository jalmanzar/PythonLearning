import unittest

class TestAddMethod(unittest.TestCase)
  def test_add(self)
    from firsttest.py import add_two
    
    result = add_two(12 ,16)
    
    self.assertTrue(result == 28)
    self.assertFalse(result != 28)
