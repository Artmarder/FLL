#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from time import ticks_ms, ticks_diff
from main import PIDController, Odometry
from .deviceManagers import (ColorSensorManager, DeviceManager, GyroSensorManager, MotorManager)

odometry = Odometry()
startOdometry = odometry.start_odometry()
getX = odometry.getX
getY = odometry.getY
getTh = odometry.getTh



class MrRobot:
    def __init__(self):
        self.Ev3 = EV3Brick()
        self.Gyro = GyroSensorManager()
        self.Motors = MotorManager(exit_exec=lambda: Button.LEFT in self.Ev3.buttons.pressed())
        self.ColorSensors = ColorSensorManager()
        self.DeviceControl = DeviceManager()
        self.Parameters = Parameters()
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.B)


    def drive(self, speed, distance, setPoint):
        pid = PIDController(5, 0.05, 0.5)
        initial_time = ticks_ms()
        initial_distance = self.calculate_distance()
        tolerance = 1
        timeout = 60000

        while fmean(abs(self.calculate_distance() - initial_distance - distance) > tolerance and (ticks_ms() - initial_time) < timeout):
            current_angle = self.Gyro.gyro_sensor.angle()
            error = setPoint - current_angle

            if error < -180:
                error += 360
            elif error > 180:
                error -= 360

            correction = pid.correction(error)
            self.left_motor.run(speed + correction)
            self.right_motor.run(speed - correction)

        self.left_motor.stop()
        self.right_motor.stop()

    def DistanceController(self, Cdistance):
        pid = PIDController(2, 0.03, 0.8)
        initial_time = ticks_ms()
        timeout = 60000
        tolerance = 1

        while abs(self.calculate_distance() - Cdistance) > tolerance and (ticks_ms() - initial_time) < timeout:
            currentDistance = self.calculate_distance()
            error = Cdistance - currentDistance
            correction = pid.correction(error)

            self.left_motor.run(self.Parameters.speed + correction)
            self.right_motor.run(self.Parameters.speed - correction)

        self.left_motor.stop()
        self.right_motor.stop()

    def speedControllerLUP(self, target_speed):
        pid = PIDController(2, 0.03, 0.8)
        initial_time = ticks_ms()
        timeout = 60000

        while (ticks_ms() - initial_time) < timeout:
            current_speed = self.calculate_speedLUP()
            speed_error = target_speed - current_speed

            correction = pid.correction(speed_error)

            self.left_motor.run(target_speed + correction)
            self.right_motor.run(target_speed + correction)

        self.left_motor.stop()
        self.right_motor.stop()

    def speedControllerRUP(self, target_speed):
        pid = PIDController(2, 0.03, 0.8)
        initial_time = ticks_ms()
        timeout = 60000

        while (ticks_ms() - initial_time) < timeout:
            current_speed = calculate_speedRUP()
            speed_error = target_speed - current_speed

            correction = pid.correction(speed_error)

            self.left_motor.run(target_speed + correction)
            self.right_motor.run(target_speed + correction)

        self.left_motor.stop()
        self.right_motor.stop()

    def TURN(self, targetTurn, speed):
        pid = PIDController(4.5, 0.09, 1)
        initial_time = ticks_ms()
        timeout = 6000

        while (ticks_ms() - initial_time) < timeout:
            current_angle = self.Gyro.gyro_sensor.angle()
            error = targetTurn - current_angle

            if error < -180:
                error += 360
            elif error > 180:
                error -= 360

            correction = pid.correction(error)

            self.left_motor.run(speed + correction)
            self.right_motor.run(speed - correction)

        self.left_motor.stop()
        self.right_motor.stop()

    
    def X(self,targetX,speed):
        pid = PIDController(8, 0.1, 0.2)
        timeout = 6000
        initial_time = ticks_ms()
        currentX = getX
        error = targetX - currenteX

        while (ticks_ms() - initial_time) < timeout:
            
            correction = pid.correction(error)

            self.left_motor.run(speed + correction)
            self.right_motor.run(speed - correction)

        self.left_motor.stop()
        self.right_motor.stop()


    def Y(self,targetY,speed):
        pid = PIDController(8, 0.1, 0.2)
        timeout = 6000
        initial_time = ticks_ms()
        currentY = getY
        error = targetY - currenteY

        while (ticks_ms() - initial_time) < timeout:
            
            correction = pid.correction(error)

            self.left_motor.run(speed + correction)
            self.right_motor.run(speed - correction)

        self.left_motor.stop()
        self.right_motor.stop()



    def Th(self,targetTh,speed):
        pid = PIDController(8, 0.1, 0.2)
        timeout = 6000
        initial_time = ticks_ms()
        currentX = getTh
        error = targetTh - currenteTh

        while (ticks_ms() - initial_time) < timeout:
            
            correction = pid.correction(error)

            self.left_motor.run(speed + correction)
            self.right_motor.run(speed - correction)

        self.left_motor.stop()
        self.right_motor.stop()




def line_follower(base_speed):
    pid = PIDController(1.2, 0.01, 0.2)
    target_reflection = 10
    initial_time = ticks_ms()
    timeout = 60000

    while (ticks_ms() - initial_time) < timeout:
        current_reflection = self.ColorSensors.get_reflection()
        error = target_reflection - current_reflection
        correction = pid.correction(error)
        self.left_motor.run(base_speed - correction)
        self.right_motor.run(base_speed + correction)



    self.left_motor.stop()
    self.right_motor.stop()
