import unittest
import os


class MyTestCase(unittest.TestCase):
    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
