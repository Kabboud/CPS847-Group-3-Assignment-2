import unittest
from functions import subtract_one

class TestSampleMethods(unittest.TestCase):
      def test_increment_by_two(self):
        """
        Test increments
        """
        self.assertEqual(subtract_one(-1), -2)
        self.assertEqual(subtract_one(0), -1)
        self.assertEqual(subtract_one(1), 0)
        self.assertEqual(subtract_one(2), 1)
        
if __name__ == '__main__':
    unittest.main()
