from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from time import sleep
from math import cos, sin, pi
from _thread import LockType

WHEEL_DIAMETER = 56
WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * pi
WHEEL_BASE = 120
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

class Odometry:
    """
    in this class we can watvh the odometry when robot drive.
    """

    def __init__(self,drivebase = drivebase x: float = 0, y: float = 0, theata: float = 0):

        self.x, self.y = x, y
        self.theata = theata

        self.drivebase = drivebase

        self.run = False
        

    def calculate_distance(degrees_rotated):
        """
        calculate the distance. 
        """
        return (degrees_rotated / 360) * WHEEL_CIRCUMFERENCE


    @micropython.native
    @thread
    def startOdometry(self):
        """
        start the odomerty .
        """
        self.run = True
        while self.run:
            def update_position(left_motor, right_motor, x, y, theta):

                left_degrees = left_motor.angle()
                right_degrees = right_motor.angle() 

                dL = calculate_distance(left_degrees)
                dR = calculate_distance(right_degrees)

                dTheta = gyro.sensor()
                d = (dR + dL) / 2

                dx = d * cos((theta + dTheta) / 2)
                dy = d * sin((theta + dTheta) / 2 ) 

                x += dx
                y += dy
                theta = dTheta

                lastTheta = theta

    @micropython.native    
    def stop(self) :
        """
        stop the odomerty. 
        """
        self.run = False
            

    def resetPostion(self, x: float = 0, y: float = 0, theata: float = 0)

            def update_file_odometry_write():
                """
                hear we comeback all Parameters to file.
                """
                odometry_file = open("odometry.txt")
                odometry_file.write("x="x,"y="y,"theta="theta)
