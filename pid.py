import micropython as micro
from time import time
from MyDevice import *
from myTools import *
from odometry import *

class PIDController:
    def init(self, kp, ki, kd, target):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.lastError = 0
        self.lastTime = time()
        self.target = target
    
    @micro.native
    def correction(self, current_angle):
        current_time = time()
        error = self.target - current_angle
        deltaTime = current_time - self.lastTime
        if deltaTime == 0:
            deltaTime += 0.001
        
        proportional = error
        self.integral += (error + self.lastError) / 2 * deltaTime
        differential = (error - self.lastError) / deltaTime if deltaTime != 0 else 0
        
        output.correction = self.kp * proportional + self.ki * self.integral + self.kd * differential
        
        self.lastError = error
        self.lastTime = current_time
        
        return pid_a

    def drive(self, speed, wantedDistance):
        current_distance = calculate_distance()

        while current_distance < wantedDistance:
            current_angle = GetAngle()
            correction = self.correction(current_angle)
            error = self.target - current_angle
            if error < -180:
                error += 360
            run_tank(speed + correction, speed - correction)
            current_distance = calculate_distance()

        motor.stop()

    def turn(self, target, speed):
        pid = PIDController(self.kp, self.ki, self.kd, target)

        while True:
            current_angle = GetAngle()
            error = target - current_angle
            if abs(error) < 1:
                break

            if error < -180:
                error += 360

            correction = pid.correction(current_angle)
            run_tank(correction, -correction)
        
        motor.stop()
