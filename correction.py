from time import ticks_diff, ticks_ms
from MyDevice import *  
from myTools import GetAngle, calculate_distance  

# good PID, i would also implement a way to input the error yourself (like i did) because 
# of the example of turining in place: e = 0 - 270 = 270, but a faster correction would be e = -90

class PIDController():
    def _init_(self, kp, ki, kd, target):
        
        self.kp = kp
        self.ki = ki
        self.kd = kd
        
        self.integral = 0
        
        self.last_error = 0
        self.last_time = ticks_ms()
        
        self.target = target

    def correction(self, current_angle):
        current_time = ticks_ms()

        # convert to seconds(important)
        delta_time = ticks_diff(current_time, self.last_time)
        if delta_time == 0:
            delta_time = 1 

        error = self.target - current_angle
        # error %= 360 does the same thing but faster
        error = (error + 360) % 360  

        # shorter var names: proportional -> p, differential -> d
        # no need for this line, put error directly in the output
        proportional = error
        self.integral += (error + self.last_error) * 0.5 * delta_time
        differential = (error - self.last_error) / delta_time

        output = self.kp * proportional + self.ki * self.integral + self.kd * differential

        self.last_error = error
        self.last_time = current_time

        return output

# Basic
# would put in its own file, or in the drivebase file (you need to create it in the futre)
class DriveBasic():
    # i would create the pid inside the function, i dont think you know what it means to declare a varible in this space
    def __init__(self, distance, speed):        
        self.distance = distance
        self.speed  = speed 
        
        setpoint = current_angle

    def drive(target_distance, speed):

        # you need to pass params to PIDController()
        PID = PIDController()
        initial_distance = calculate_distance()

        while (calculate_distance() - initial_distance) < target_distance:
            current_angle = GetAngle()
            
            # once again, if the target is 0 and angle is 270, it would turn 270 degrees instead of -90
            # bad
            # fix
            correction = self.correction(current_angle)
            run_tank(speed + correction, speed - correction)

        motor.stop()

    def turn(self, target_angle, speed):
        # you need to pass params to PIDController()
        PID = PIDController()
        while True:

            current_angle = GetAngle()

            # youre calculating error 2 times
            # what i did is in PIDController when calculating the error i did self.error = ...
            # then i got the error by PID.error
            # again, the error thingy
            # once again, if the target is 0 and angle is 270, it would turn 270 degrees instead of -90
            error = target_angle - current_angle
            # error %= 360 does the same thing but faster
            error = (error + 360) % 360 

            #put this in the while loop
            if abs(error) < 1:
                break
    
            correction = self.correction(current_angle)
            # add speed
            run_tank(correction, -correction)
    
    
        motor.stop()
