from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from time import sleep
from math import cos, sin, pi

WHEEL_DIAMETER = 56
WHEEL_CIRCUMFERENCE = WHEEL_ DIAMETER * pi
WHEEL_BASE = 120

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

class Odometry:
    """
    This class implements odometry for an EV3 robot in FLL competitions.
    """

    def _init_(self, drivebase: DriveBase):
        """
        Initializes the odometry object.

        Args:
            drivebase: The DriveBase object representing the robot's motors.
        """

        self.x = 0.0  # Initial X position (mm)
        self.y = 0.0  # Initial Y position (mm)
        self.theta = 0.0  # Initial angle (radians)

        self.drivebase = drivebase

        self.last_left_angle = 0  # Stores previous left motor angle for delta calculation
        self.last_right_angle = 0  # Stores previous right motor angle for delta calculation
        self.running = False  # Flag to control odometry loop

    def start_odometry(self):
        """
        Starts the odometry loop. This method should be called
        after robot movement commands to track the position.
        """

        self.running = True
        while self.running:
            left_angle = left_motor.angle()
            right_angle = right_motor.angle()

            delta_left = (left_angle - self.last_left_angle) * 360 / (WHEEL_CIRCUMFERENCE * self.drivebase.gears.ratio)  # Convert to degrees and account for gear ratio
            delta_right = (right_angle - self.last_right_angle) * 360 / (WHEEL_CIRCUMFERENCE * self.drivebase.gears.ratio)

            self.last_left_angle = left_angle
            self.last_right_angle = right_angle

            # Average delta angles for more accurate heading calculation
            delta_theta = (delta_left + delta_right) / 2

            # Calculate distance traveled based on average delta angle
            distance = (delta_left + delta_right) / 2 * WHEEL_CIRCUMFERENCE / self.drivebase.gears.ratio

            # Update position using trigonometry and considering robot orientation
            dx = distance * cos((self.theta + delta_theta) / 2)
            dy = distance * sin((self.theta + delta_theta) / 2)

            self.x += dx
            self.y += dy
            self.theta += delta_theta

            sleep(0.01)  # Short delay for smoother updates

    def stop_odometry(self):
        """
        Stops the odometry loop.
        """

        self.running = False

    def reset_position(self, x=0.0, y=0.0, theta=0.0):
        """
        Resets the robot's estimated position and orientation.

        Args:
            x: New X position (mm).
            y: New Y position (mm).
            theta: New angle (radians).
        """

        self.x = x
        self.y = y
        self.theta = theta

        # Reset motor angle tracking for accurate deltas
        self.last_left_angle = left_motor.angle()
        self.last_right_angle = right_motor.angle()
     
    self.x,self.y,self.theata = x, y, theata


"""
BLUE PHOENIX CODE 
"""
