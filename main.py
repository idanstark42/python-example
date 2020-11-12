#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

from gyro import turn

from run1 import run1
from run2 import run2

# Creating objects
right = Motor(Port.B)
left = Motor(Port.C)
drive_base = DriveBase(left, right, 55.5, 124)

# Starting the program
turn(90, 60, Port.S4, drive_base)
drive_base.straight(200) # 20 cm

run1(drive_base)
run2(drive_base)