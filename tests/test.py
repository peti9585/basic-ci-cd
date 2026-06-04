import unittest
import main

class AddTestCase(unittest.TestCase):
    def test_add_success(self):
        expected_value = 5
        actual_value = main.add(3, 2)

        self.assertEqual(expected_value, actual_value)

if __name__ == '__main__':
    unittest.main()
