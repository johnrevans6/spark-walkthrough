import unittest

class Lab02_Tests(unittest.TestCase):
  def part_a(self, top_10):
    expected = -5571471231038731392
    self.assertEqual(hash(str(top_10)), 
                      expected, 
                      'Try Again! Remember to only include words strictly greater than three characters long.')
  
  def part_b(self, rows):
    expected = 663250
    self.assertEqual(rows, 
                      expected, 
                      'Try Again! Remember to flatten the input before converting to a DataFrame')
  
if  __name__ == '__main__':
  unittest.main() 