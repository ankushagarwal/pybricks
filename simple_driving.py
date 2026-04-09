from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

hub = PrimeHub()

drive_motor = Motor(Port.A)
steering_motor = Motor(Port.C)

# Approximate conversion from block % values to motor speed in deg/s.
DRIVE_SPEED_SCALE = 10
STEERING_SPEED = 750  # about 75%
MAX_STEERING_ANGLE = 35  # from the block: steering * 35 / 100


def drive_at_speed_while_steering(speed_percent, steering_percent):
    steering_target = steering_percent * MAX_STEERING_ANGLE / 100
    steering_motor.run_target(STEERING_SPEED, steering_target, wait=False)
    drive_motor.run(-speed_percent * DRIVE_SPEED_SCALE)


# Center steering first.
steering_motor.run_target(STEERING_SPEED, 0)

# Let drive motor coast when stopped.
drive_at_speed_while_steering(70, 50)
wait(2000)

# drive_at_speed_while_steering(-70, 0)
# wait(2000)

# drive_at_speed_while_steering(50, 100)
# wait(1000)

# drive_at_speed_while_steering(50, -100)
# wait(1000)

drive_motor.stop()
steering_motor.run_target(STEERING_SPEED, 0, then=Stop.HOLD)

drive_at_speed_while_steering(-70, 50)
wait(2000)
steering_motor.run_target(STEERING_SPEED, 0)
