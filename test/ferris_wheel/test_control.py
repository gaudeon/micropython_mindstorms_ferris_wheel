import usys
import unittest

class MockConfig:
    def __init__(self):
        self.max_degrees = 10
        self.speed_limit = 10
        self.speed_increment = 1

class MockMotor:
    def __init__(self, speed):
        self.speed = speed

    def get_position(self):
        return self.speed

usys.path.insert(0, 'src')
usys.path.insert(0, 'mock')

from ferris_wheel.control import FerrisWheelControl

class TestFerrisWheelControl(unittest.TestCase):
    def test_get_speed(self):
        ferris_wheel_config = MockConfig()
        motor = MockMotor(5)
        expected = 5

        ferris_wheel_control = FerrisWheelControl(motor, ferris_wheel_config)
        speed = ferris_wheel_control.get_speed()

        self.assertEqual(speed, expected, "ferris wheel control get speed returns correct result")

if __name__ == '__main__':
    unittest.main()