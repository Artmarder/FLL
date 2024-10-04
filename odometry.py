#!/usr/bin/env pybricks-micropython
from time import sleep
from math import cos, sin
from mytools import thread
from _thread import allocate_lock
from math import radians

class Odometry:
    """
    This class implements odometry for an EV3 robot in FLL competitions.
    """
    def __init__(self, drivebase):
        """
        Initializes the odometry object.

        Args:
            drivebase: The DriveBase object representing the robot's motors.
        """

        self.x = 0.0  # Initial X position (mm)
        self.y = 0.0  # Initial Y position (mm)
        self.theta = 0.0  # Initial angle (radians)

        self.running = False  # Flag to control the odometry loop

        self.drivebase = drivebase

        self.lock = allocate_lock()


    @thread
    def start_odometry(self):
        """
        Starts the odometry loop. This method should be called
        after robot movement commands to track the position.
        """

        self.running = True
        while self.running:
            left_angle = self.drivebase.leftMotor.angle()
            right_angle = self.drivebase.rightMotor.angle()

            # Compute the changes in wheel angles in mm
            delta_left = (left_angle - self.last_left_angle) * self.WHEEL_CIRCUMFERENCE / 360
            delta_right = (right_angle - self.last_right_angle) * self.WHEEL_CIRCUMFERENCE / 360

            # Update motor angles
            self.last_left_angle = left_angle
            self.last_right_angle = right_angle

            # Compute the average change in angle
            theta = self.drivebase.gyro.angle()
            # Compute the distance traveled
            distance = (delta_left + delta_right) / 2

            # Update position considering robot orientation
            theta_radians = radians(theta)
            dx = distance * cos(theta_radians)
            dy = distance * sin(theta_radians)

            with self.lock:
                self.x += dx
                self.y += dy
                self.theta = theta

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

        with self.lock:
            self.x = x
            self.y = y
            self.theta = theta

    def getPoseX(self):
        with self.lock:
            return self.x
        
    def getPoseY(self):
        with self.lock:
            return self.y
        
    def getPoseTheta(self):
        with self.lock:
            return self.theta
        
    


