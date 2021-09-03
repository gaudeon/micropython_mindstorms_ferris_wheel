from mindstorms import Motor
import math

class FerrisWheelControl:
    def __init__(self, control_motor:Motor, config:FerrisWheelConfig):
        self.config = config
        self.control_motor = control_motor

    def get_speed(self):
        degrees = self.control_motor.get_position()

        speed = math.floor(degrees / self.config.max_degrees * self.config.speed_limit / self.config.speed_increment) * self.config.speed_increment

        return speed