import unittest
from pyspark.sql import Row

class Lab01_Tests(unittest.TestCase):
  def part_a(self, scheduler):
    expected = 'FIFO'
    self.assertEqual(hash(scheduler.upper()), 
                      hash(expected), 
                      'Try Again! The answer you\'re looking for is located at localhost:4040/environment')
  
  def part_b(self, version):
    expected = '2.4.6'
    self.assertEqual(hash(version), 
                     hash(expected),
                     'Try Again! Look in the upper left corner of the Spark UI. What do you see?')
  
  def part_c(self, path):
    expected = '/var/log/ipnb'
    self.assertEqual(hash(path), 
                     hash(expected),
                     'Try Again! The answer you\'re looking for is located at localhost:4040/environment')
  
  def part_d(self, rdd):
    expected_rdd = [('n', 6), ('a', 5), ('i', 5), ('l', 4), ('h', 2), ('e', 2), 
                    ('p', 2), ('t', 1), ('r', 1), ('s', 1), ('f', 1), ('s', 1), 
                    ('m', 1), ('y', 1), ('o', 1), ('t', 1)]

    self.assertEqual(hash(rdd), hash(expected_rdd), 'Try Again! Remember, we want to sort from highest occurence to lowest occurrence')
  
  def part_e(self, most_used, least_used):
    expected_most_used = 1800308978868044819
    
    expected_least_used = 3069037530674927221
    
    """
    SELECT word, COUNT(word) as count
             FROM word_count
             GROUP BY word ORDER BY count DESC
    """
    self.assertEqual(hash(str(most_used)), expected_most_used, 'Try Again! The most used words can be found using ORDER BY DESC')
    """
    SELECT word, COUNT(word) as count
             FROM word_count
             GROUP BY word ORDER BY count
    """
    self.assertEqual(hash(str(least_used)), expected_least_used, 'Try Again! The least used words can be found using ORDER BY')

if  __name__ == '__main__':
  unittest.main() 