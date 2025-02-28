#!/usr/bin/env pybricks-micropython
from MrRobot import MrRobot
from driveBsae import Drivebase
from PID import PIDController
from time import sleep
from pybricks.tools import wait
drivebase = Drivebase()
mrRobot = MrRobot(drivebase)    

class RUNS:
    def __init__(self, mrRobot):
        self.mrRobot = mrRobot
        self.Drivebase = Drivebase()
    def run1(self):
        self.mrRobot.PIDDriveForward(400, 70, 0,7,0.00004,2.5)
        self.mrRobot.Run_Tank_Motors_samll(-55,96)
        self.mrRobot.PIDDriveBack(-400, -70, 0,7,0.00004,2.5)

    def run2(self):
        self.mrRobot.PIDDriveForward(450,24,0,3.2,0.00004,2.5)
        self.mrRobot.TurnMinus(-89,2,0,0)
        self.mrRobot.PIDDriveForward(450,51,-90,3.2,0.00004,2.5)
        self.mrRobot.TurnMinus(-41,2.5,0,0)
        self.mrRobot.PIDDriveForward(450,8.3,-41,3.2,0.00004,2.5)
        self.mrRobot.PIDDriveBack(-400, -10, -41,3.2,0.00004,2.5)
        self.mrRobot.TurnMinus(-33,2.5,0,0)
        self.mrRobot.PIDDriveForward(450,10,-37,3.2,0.00004,2.5)
        self.mrRobot.forwardMotor1(350,90)
        self.mrRobot.PIDDriveBack(-400, -3, -41,3.2,0.00004,2.5)
        self.mrRobot.TurnMinus(-81,2.5,0,0)
        self.mrRobot.PIDDriveForward(450,100,-37,3.2,0.00004,2.5)



    def run5(self):
        self.mrRobot.PIDDriveForward(450,72,0,1,0.0004,4)
        self.Drivebase.resetGyro(0)
        self.mrRobot.Turn(32,1,0,0)
        wait(1000)
        self.Drivebase.resetGyro(0)
        self.mrRobot.PIDDriveForward(450,19,32,1,0.0004,4)
        self.Drivebase.resetGyro(0)
        self.mrRobot.PIDDriveBack(-400, -6, 32,3.2,0.00004,2.5)
