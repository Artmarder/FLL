from time import ticks_ms, ticks_diff

class PIDController():
    def __init__(self, kp, ki, kd, target):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.last_error = 0
        self.last_time = ticks_ms()
        self.target = target

    def correction(self, current_angle):
        current_time = ticks_ms()
        delta_time = ticks_diff(current_time, self.last_time)
        if delta_time == 0:
            delta_time = 1 
        delta_time /= 1000

        error = self.target - current_angle
        error = (error + 180) % 360 - 180  

        proportional = error
        self.integral += (error + self.last_error) / 2 * delta_time
        differential = (error - self.last_error) / delta_time

        output = self.kp * proportional + self.ki * self.integral + self.kd * differential

        self.last_error = error
        self.last_time = current_time

        return output
