import usys
import unittest

usys.path.insert(1, 'src')
from ferris_wheel.config import FerrisWheelConfig

class TestFerrisWheel(unittest.TestCase):
    def setup(self):
        pass
    
    def test_assert(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()