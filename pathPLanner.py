from math import atan2, pi

class PathController:
    def __init__(self, odometry, drivebase, Kp: float, Ki: float, Kd: float):
        self.odometry = odometry
        self.drivebase = drivebase
        self.pid = PIDController(Kp, Ki, Kd)

    def reset_odometry(self):
        self.odometry.stop_odometry()
        self.odometry.reset_position(0, 0, 0)
        self.odometry.start_odometry()

    def calculate_angle_correction(self, target_x: float, target_y: float) -> float:
        current_x = self.odometry.getPoseX()
        current_y = self.odometry.getPoseY()
        theta = self.odometry.getPoseTheta()
        
        target_angle = atan2(target_y - current_y, target_x - current_x)
        angle_error = target_angle - theta
        
        if angle_error > pi:
            angle_error -= 2 * pi
        elif angle_error < -pi:
            angle_error += 2 * pi
        
        return self.pid.correction(angle_error)

    def follow_path(self, waypoints: list, max_speed: float):
        for target_x, target_y in waypoints:
            while True:
                angle_correction = self.calculate_angle_correction(target_x, target_y)
                forward_speed = max_speed
                turn_speed = angle_correction
                
                SpeedMotorLeft = forward_speed + turn_speed
                SpeedMotorRight = forward_speed - turn_speed
                
                self.drivebase.run_tank(SpeedMotorLeft, SpeedMotorRight)
