from pybricks.hubs import EV3Brick
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Direction
from pybricks.tools import wait

def turn(angle, max_speed, gyro_port, drive_base):
    gyro = GyroSensor(gyro_port, Direction.COUNTERCLOCKWISE)
    ev3 = EV3Brick()
    ev3.screen.clear()

    initial_error = gyro.angle() - angle

    while abs(gyro.angle() - angle) > 2:
        error = gyro.angle() - angle
        speed = max_speed * (error / initial_error)
        ev3.screen.print(gyro.angle(), error, speed)
        drive_base.drive(0, speed)
        wait(10)
