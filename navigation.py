from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

hub = PrimeHub()

drive_motor = Motor(Port.A)
distance_sensor = UltrasonicSensor(Port.B)
steering_motor = Motor(Port.C)
scanner_motor = Motor(Port.D)

DRIVE_SPEED_SCALE = 10
STEERING_SPEED = 750
SCANNER_SPEED = 750
MAX_STEERING_ANGLE = 35


def midi_to_hz(note):
    return round(440 * (2 ** ((note - 69) / 12)))


def go_to_shortest_position(motor, speed, target):
    current = motor.angle()
    nearest_target = target + 360 * round((current - target) / 360)
    motor.run_target(speed, nearest_target)


def drive_at_speed_while_steering(speed_percent, steering_percent):
    steering_target = steering_percent * MAX_STEERING_ANGLE / 100
    go_to_shortest_position(steering_motor, STEERING_SPEED, steering_target)
    drive_motor.run(-speed_percent * DRIVE_SPEED_SCALE)


def honk():
    hub.speaker.beep(midi_to_hz(76), 50)
    hub.speaker.beep(midi_to_hz(79), 100)
    wait(100)
    hub.speaker.beep(midi_to_hz(76), 50)
    hub.speaker.beep(midi_to_hz(79), 500)


def look_around():
    go_to_shortest_position(scanner_motor, SCANNER_SPEED, 80)
    dist_right = distance_sensor.distance() / 10

    go_to_shortest_position(scanner_motor, SCANNER_SPEED, 280)
    dist_left = distance_sensor.distance() / 10

    if dist_left > dist_right:
        go_to_shortest_position(scanner_motor, SCANNER_SPEED, 280)
        drive_at_speed_while_steering(-50, 100)
        wait(1000)
        drive_motor.stop()
        drive_at_speed_while_steering(50, -100)
        wait(1500)
    else:
        go_to_shortest_position(scanner_motor, SCANNER_SPEED, 80)
        drive_at_speed_while_steering(-50, -100)
        wait(1000)
        drive_motor.stop()
        drive_at_speed_while_steering(50, 100)
        wait(1500)

    go_to_shortest_position(scanner_motor, SCANNER_SPEED, 0)


scanner_motor.control.limits(speed=SCANNER_SPEED)
go_to_shortest_position(scanner_motor, SCANNER_SPEED, 0)
drive_motor.stop()


while True:
    drive_at_speed_while_steering(50, 0)

    while distance_sensor.distance() >= 200:
        wait(200)

    drive_motor.stop()
    honk()
    look_around()
