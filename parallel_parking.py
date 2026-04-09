from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Side
from pybricks.tools import wait

hub = PrimeHub()

drive_motor = Motor(Port.A)
distance_sensor = UltrasonicSensor(Port.B)
steering_motor = Motor(Port.C)
scanner_motor = Motor(Port.D)

DRIVE_SPEED = 250
STEERING_SPEED = 750
SCANNER_SPEED = 750


def midi_to_hz(note):
    return round(440 * (2 ** ((note - 69) / 12)))


def go_to_shortest_position(motor, speed, target):
    current = motor.angle()
    nearest_target = target + 360 * round((current - target) / 360)
    motor.run_target(speed, nearest_target)


def wait_until_bottom_up():
    while hub.imu.up() != Side.BOTTOM:
        wait(10)


def wait_until_closer_than(distance_mm):
    while distance_sensor.distance() >= distance_mm:
        wait(10)


def wait_until_farther_than(distance_mm):
    while distance_sensor.distance() <= distance_mm:
        wait(10)


def beep_note(note):
    hub.speaker.beep(midi_to_hz(note), 100)


def drive_forward():
    drive_motor.run(-DRIVE_SPEED)


def drive_forward_degrees(degrees):
    drive_motor.run_angle(DRIVE_SPEED, -degrees)


def drive_backward_degrees(degrees):
    drive_motor.run_angle(DRIVE_SPEED, degrees)


def find_spot():
    go_to_shortest_position(scanner_motor, SCANNER_SPEED, 80)
    go_to_shortest_position(steering_motor, STEERING_SPEED, 0)

    drive_motor.reset_angle(0)
    drive_forward()

    wait_until_closer_than(150)
    beep_note(72)
    wait(500)

    wait_until_farther_than(300)
    beep_note(76)
    wait(500)

    wait_until_closer_than(150)
    beep_note(79)

    drive_forward_degrees(290)


def park():
    go_to_shortest_position(steering_motor, STEERING_SPEED, 45)
    drive_backward_degrees(460)

    go_to_shortest_position(steering_motor, STEERING_SPEED, 0)
    drive_backward_degrees(130)

    go_to_shortest_position(steering_motor, STEERING_SPEED, 315)
    drive_backward_degrees(210)

    go_to_shortest_position(steering_motor, STEERING_SPEED, 45)
    drive_forward_degrees(60)

    go_to_shortest_position(steering_motor, STEERING_SPEED, 315)
    drive_backward_degrees(90)

    go_to_shortest_position(steering_motor, STEERING_SPEED, 45)
    drive_forward_degrees(60)

    go_to_shortest_position(steering_motor, STEERING_SPEED, 0)
    drive_backward_degrees(40)

    go_to_shortest_position(scanner_motor, SCANNER_SPEED, 0)


go_to_shortest_position(steering_motor, STEERING_SPEED, 0)
wait_until_bottom_up()
wait(3000)

find_spot()
park()
