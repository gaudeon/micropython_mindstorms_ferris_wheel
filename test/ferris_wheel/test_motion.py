import usys
import unittest

usys.path.insert(1, 'src')
usys.path.insert(0, 'mock')

from ferris_wheel.motion import FerrisWheelMotion

class MockConfig:
    def __init__(self):
        self.max_degrees = 10
        self.speed_limit = 10
        self.speed_increment = 1

class MockMotor:
    def __init__(self):
        self.motor_started = False
        self.motor_speed = 0

    def start(self, speed):
        self.motor_started = True
        self.motor_speed = speed


class TestFerrisWheelMotion(unittest.TestCase):
    def test_rotate_forward(self):
        ferris_wheel_config = MockConfig()
        left_motor = MockMotor()
        right_motor = MockMotor()
        expected_left_motor_speed = -5
        expected_right_motor_speed = 5

        ferris_wheel_motion = FerrisWheelMotion(left_motor, right_motor, ferris_wheel_config)
        ferris_wheel_motion.rotate_forward(5)

        self.assertEqual(left_motor.motor_speed, expected_left_motor_speed, "ferris wheel motion set left motor to the correct speed")
        self.assertTrue(left_motor.motor_started, "ferris wheel motion started left motor")

        self.assertEqual(right_motor.motor_speed, expected_right_motor_speed, "ferris wheel motion set right motor to the correct speed")
        self.assertTrue(right_motor.motor_started, "ferris wheel motion started right motor")

    def test_rotate_reverse(self):
        ferris_wheel_config = MockConfig()
        left_motor = MockMotor()
        right_motor = MockMotor()
        expected_left_motor_speed = 5
        expected_right_motor_speed = -5

        ferris_wheel_motion = FerrisWheelMotion(left_motor, right_motor, ferris_wheel_config)
        ferris_wheel_motion.rotate_reverse(5)

        self.assertEqual(left_motor.motor_speed, expected_left_motor_speed, "ferris wheel motion set left motor to the correct speed")
        self.assertTrue(left_motor.motor_started, "ferris wheel motion started left motor")

        self.assertEqual(right_motor.motor_speed, expected_right_motor_speed, "ferris wheel motion set right motor to the correct speed")
        self.assertTrue(right_motor.motor_started, "ferris wheel motion started right motor")

if __name__ == '__main__':
    unittest.main()