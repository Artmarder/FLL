import micropython as micro
from time import time as time
from MyDevice import all
from myTools.py import all
from odomerty import all

class PIDController():
    def __init__(self, kp, ki, kd, error, feedback, target) -> float:
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.error = error
        self.feedback = feedback
        self.lastError = lastError = 0
        self.lastTime = time()
        self.target = target
    
    
    @micro.native
    def correction():

        error = target - GetAngel

        
        deltaTime = time - lastTime
        
        proportional = error
        integral += (error + lastError) / 2 * deltaTime
        differential = (error - lastError) / deltaTime

        return kp * proportional + ki * integral + kd * differential


    def drive(speed, wantedDistance) -> float:
        correction = correction()
        Distance = calculate_distance()

        while Distance > wantedDistance:
            if speed > 0:
                error = target - GetAngel
                if error < -180:
                error += 360
                run_tank(speed+correction, speed - correction)

        motor.stop