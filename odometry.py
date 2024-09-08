#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from time import sleep
from math import cos, sin, pi

WHEEL_DIAMETER = 56  # Wheel diameter in mm
WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * pi  # Wheel circumference in mm
WHEEL_BASE = 120  # Distance between wheels in mm

# Initialize motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize DriveBase
drivebase = DriveBase(left_motor, right_motor, WHEEL_BASE, WHEEL_DIAMETER)

class Odometry():
    """
    This class implements odometry for an EV3 robot in FLL competitions.
    """

    def __init__(self, drivebase: DriveBase):
        """
        Initializes the odometry object.

        Args:
            drivebase: The DriveBase object representing the robot's motors.
        """

        self.x = 0.0  # Initial X position (mm)
        self.y = 0.0  # Initial Y position (mm)
        self.theta = 0.0  # Initial angle (radians)

        self.drivebase = drivebase

        # Initialize last motor angles
        self.last_left_angle = left_motor.angle()
        self.last_right_angle = right_motor.angle()
        self.running = False  # Flag to control the odometry loop

    def start_odometry(self):
        """
        Starts the odometry loop. This method should be called
        after robot movement commands to track the position.
        """

        self.running = True
        while self.running:
            try:
                left_angle = left_motor.angle()
                right_angle = right_motor.angle()

                # Compute the changes in wheel angles in mm
                delta_left = (left_angle - self.last_left_angle) * WHEEL_CIRCUMFERENCE / 360
                delta_right = (right_angle - self.last_right_angle) * WHEEL_CIRCUMFERENCE / 360

                # Update motor angles
                self.last_left_angle = left_angle
                self.last_right_angle = right_angle

                # Compute the average change in angle
                delta_theta = (delta_right - delta_left) / WHEEL_BASE
                # Compute the distance traveled
                distance = (delta_left + delta_right) / 2

                # Update position considering robot orientation
                dx = distance * cos(self.theta + delta_theta / 2)
                dy = distance * sin(self.theta + delta_theta / 2)

                self.x += dx
                self.y += dy
                self.theta += delta_theta

                sleep(0.01)  # Short delay for smoother updates

            except Exception as e:
                self.stop_odometry()

                print(x)
                print(y)
                print(theta)

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

        self.last_left_angle = left_motor.angle()
        self.last_right_angle = left_motor.angle()

    def getX(self):
        self.x = x
        return x

    def getY(self):
        self.y = y
        return y

    def getXTh(self):
        self.theta = theta
        return x

