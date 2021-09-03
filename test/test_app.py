import usys
import unittest

usys.path.insert(1, 'src')
usys.path.insert(0, 'mock')

import app 

class TestApp(unittest.TestCase):
    def test_main(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()