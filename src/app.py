from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

SPEED_LIMIT = 100
SPEED_INCREMENT = 10
MAX_DEGREES = 359
CHECK_BUTTON_PRESS_WAIT_SECONDS = 2

class FerrisWheelConfig:
    speed_limit = 100
    speed_increment = 10
    max_degrees = 359
    check_button_press_wait_seconds = 2

class FerrisWheelMotion:
    def __init__(self, left_motor:Motor, right_motor:Motor, config:FerrisWheelConfig):
        self.config = config
        self.right_motor = right_motor
        self.left_motor = left_motor
        self.power = 0

    def rotate_forward(self, speed:int):
        calc_speed = abs(speed)
        calc_speed = math.ceil(speed / self.config.speed_increment) * self.config.speed_increment
        if calc_speed > self.config.speed_limit:
            calc_speed = self.config.speed_limit
        self.right_motor.start(calc_speed)
        self.left_motor.start(-calc_speed)
    
    def rotate_reverse(self, speed:int):
        calc_speed = abs(speed)
        calc_speed = math.ceil(speed / self.config.speed_increment) * self.config.speed_increment
        if calc_speed > self.config.speed_limit:
            calc_speed = self.config.speed_limit
        self.right_motor.start(-calc_speed)
        self.left_motor.start(calc_speed)

class FerrisWheelControl:
    def __init__(self, control_motor:Motor, config:FerrisWheelConfig):
        self.config = config
        self.control_motor = control_motor

    def get_speed(self):
        degrees = self.control_motor.get_position()

        speed = math.floor(degrees / self.config.max_degrees * self.config.speed_limit / self.config.speed_increment) * self.config.speed_increment

        return speed

def main():
    print("starting...")

    hub = MSHub()
    right_motor = Motor('A')
    left_motor = Motor('E')
    control_motor = Motor('F')

    ferris_wheel_config = FerrisWheelConfig()

    ferris_wheel_motion = FerrisWheelMotion(left_motor, right_motor, ferris_wheel_config)

    ferris_wheel_control = FerrisWheelControl(control_motor, ferris_wheel_config)

    move_forward = True
    check_button_timer = Timer()

    current_speed = 0

    for x in range(44, 123):
        hub.speaker.beep(x)

    update_movement = False
    while True:
        new_speed = ferris_wheel_control.get_speed()

        if (check_button_timer.now() > ferris_wheel_config.check_button_press_wait_seconds and (hub.left_button.was_pressed() or hub.right_button.was_pressed())):
            check_button_timer.reset()
            move_forward = not move_forward
            update_movement = True

        if new_speed != current_speed:
            current_speed = new_speed
            update_movement = True

        if update_movement:
            update_movement = False

            if move_forward:
                ferris_wheel_motion.rotate_forward(current_speed)
            else:
                ferris_wheel_motion.rotate_reverse(current_speed)

# run the thing
#main()