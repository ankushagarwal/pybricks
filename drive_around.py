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
CRUISE_SPEED = 70
STEERING_SPEED = 750
SCANNER_SPEED = 750
MAX_STEERING_ANGLE = 35

FRONT_CLEARANCE = 180
SCAN_ANGLE = 80
BACKUP_ANGLE = 220
TURN_DRIVE_ANGLE = 320


def go_to_shortest_position(motor, speed, target):
    current = motor.angle()
    nearest_target = target + 360 * round((current - target) / 360)
    motor.run_target(speed, nearest_target)


def drive_at_speed_while_steering(speed_percent, steering_percent):
    steering_target = steering_percent * MAX_STEERING_ANGLE / 100
    steering_motor.run_target(STEERING_SPEED, steering_target, wait=False)
    drive_motor.run(-speed_percent * DRIVE_SPEED_SCALE)


def look_straight():
    go_to_shortest_position(scanner_motor, SCANNER_SPEED, 0)


def steer_straight():
    steering_motor.run_target(STEERING_SPEED, 0, then=Stop.HOLD)


def steer_left():
    steering_motor.run_target(STEERING_SPEED, -MAX_STEERING_ANGLE, then=Stop.HOLD)


def steer_right():
    steering_motor.run_target(STEERING_SPEED, MAX_STEERING_ANGLE, then=Stop.HOLD)


def read_distance_at(angle):
    go_to_shortest_position(scanner_motor, SCANNER_SPEED, angle)
    wait(120)
    return distance_sensor.distance()


def drive_backward_degrees(degrees):
    drive_motor.run_angle(CRUISE_SPEED * DRIVE_SPEED_SCALE, degrees, then=Stop.COAST)


def drive_forward_degrees(degrees):
    drive_motor.run_angle(CRUISE_SPEED * DRIVE_SPEED_SCALE, -degrees, then=Stop.COAST)


def choose_direction():
    dist_right = read_distance_at(SCAN_ANGLE)
    dist_left = read_distance_at(-SCAN_ANGLE)
    look_straight()

    if dist_left > dist_right:
        return "left"
    return "right"


def avoid_obstacle():
    drive_motor.stop()
    hub.speaker.beep(700, 80)

    direction = choose_direction()

    if direction == "left":
        hub.speaker.beep(500, 70)
        steer_right()
        drive_backward_degrees(BACKUP_ANGLE)
        steer_left()
        drive_forward_degrees(TURN_DRIVE_ANGLE)
    else:
        hub.speaker.beep(900, 70)
        steer_left()
        drive_backward_degrees(BACKUP_ANGLE)
        steer_right()
        drive_forward_degrees(TURN_DRIVE_ANGLE)

    drive_motor.stop()
    steer_straight()
    look_straight()


steer_straight()
look_straight()
wait(500)

while True:
    drive_at_speed_while_steering(CRUISE_SPEED, 0)

    while distance_sensor.distance() >= FRONT_CLEARANCE:
        wait(10)

    avoid_obstacle()
