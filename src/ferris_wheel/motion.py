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