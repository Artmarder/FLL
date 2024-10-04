#!/usr/bin/env pybricks-micropython
from MrRobot import MrRobot
from drivebase import Drivebase
from odometry import Odometry

drivebase = Drivebase()
odometry = Odometry(drivebase)

mrRobot = MrRobot(drivebase, odometry)

class RUNS:
    def __init__(self, mrRobot):
        self.mrRobot = mrRobot

    def run1(self,):
        self.mrRobot.drivebase.resetGyro(0)
        self.mrRobot.drivebase.resetDistance()
        mrRobot.PIDDrive(900,90,0)
       
runs = RUNS(mrRobot)
runs.run1()
