#!/usr/bin/env pybricks-micropython
from MrRobot import MrRobot
from drivebase import Drivebase
from odometry import Odometry
from runs import RUNS

drivebase = Drivebase()
odometry = Odometry(drivebase)

mrRobot = MrRobot(drivebase, odometry)
runner = RUNS(mrRobot)

runner.run1()
