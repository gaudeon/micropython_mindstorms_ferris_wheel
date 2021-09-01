import usys
import unittest

usys.path.insert(1, 'src')
from ferris_wheel.config import FerrisWheelConfig

class TestFerrisWheelConfig(unittest.TestCase):
    def setup(self):
        pass
    
    def test_speed_limit(self):
        ferris_wheel_config = FerrisWheelConfig()
        self.assertTrue(ferris_wheel_config.speed_limit > 0 and ferris_wheel_config.speed_limit <= 100, "speed_limit config is within acceptable range")
    
    def test_speed_increment(self):
        ferris_wheel_config = FerrisWheelConfig()
        self.assertTrue(ferris_wheel_config.speed_increment > 0 and ferris_wheel_config.speed_increment <= 100, "speed_increment config is within acceptable range")
    
    def test_max_degrees(self):
        ferris_wheel_config = FerrisWheelConfig()
        self.assertTrue(ferris_wheel_config.max_degrees > 0 and ferris_wheel_config.max_degrees <= 360, "max_degrees config is within acceptable range")
    
    def test_check_button_press_wait_seconds(self):
        ferris_wheel_config = FerrisWheelConfig()
        self.assertTrue(ferris_wheel_config.check_button_press_wait_seconds > 0, "check_button_press_wait_seconds config is within acceptable range")

if __name__ == '__main__':
    unittest.main()