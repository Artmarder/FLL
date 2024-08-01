from MyDevice import Gyro, Motor
from myTools import Thread,Timer
from ODometry import Odometry
from correction import PIDController

class Runner:

    def __init__(self):
        self.odometry = Odometry
        self.pid = PIDController
        self.LeftMootr = Motor(self.motorA)
        self.RighrMootr = Motor(self.motorB)
        

        
