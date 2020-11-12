from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color

def run1(drive_base):
    drive_base.striaght(200)
    arm = Motor(Port.A)
    arm.run_time(360, 1, then=Stop.HOLD, wait=true)
    drive_base.striaght(-200)