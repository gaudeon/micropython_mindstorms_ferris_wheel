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
