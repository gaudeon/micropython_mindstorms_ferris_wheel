import usys
import unittest

usys.path.insert(1, 'src')
from ferris_wheel.config import FerrisWheelConfig

class TestFerrisWheelConfig(unittest.TestCase):
    def setup(self):
        pass
    
    def test_object(self):
        ferris_wheel_config = FerrisWheelConfig()
        self.assertTrue(ferris_wheel_config.speed_limit > 0 and ferris_wheel_config.speed_limit <= 100, "speed_limit config is within acceptable range")

if __name__ == '__main__':
    unittest.main()