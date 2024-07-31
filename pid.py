import micropython as micro
from time import ticks_diff, ticks_ms
from MyDevice import *  
from myTools import GetAngle, calculate_distance  

class PIDController:
    def __init__(self, kp, ki, kd, target):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.last_error = 0
        self.last_time = ticks_ms()
        self.target = target

    @micro.native
    def correction(self, current_angle):
        current_time = ticks_ms()
        delta_time = ticks_diff(current_time, self.last_time)
        if delta_time == 0:
            delta_time = 1 

        error = self.target - current_angle
        error = (error + 360) % 360  

        proportional = error
        self.integral += (error + self.last_error) * 0.5 * delta_time
        differential = (error - self.last_error) / delta_time if delta_time != 0 else 0

        output = self.kp * proportional + self.ki * self.integral + self.kd * differential
        self.last_error = error
        self.last_time = current_time

        return output

    def drive(self, speed, target_distance):
        initial_time = ticks_ms()
        initial_distance = calculate_distance()

        while calculate_distance() - initial_distance < target_distance:
            current_angle = GetAngle()
            correction = self.correction(current_angle)
            run_tank(speed + correction, speed - correction)

        motor.stop()

    def turn(self, target_angle, speed):
        while True:
            current_angle = GetAngle()
            error = target_angle - current_angle
            error = (error + 360) % 360 

            if abs(error) < 1:
                break

            correction = self.correction(current_angle)
            run_tank(correction, -correction)


        motor.stop()
