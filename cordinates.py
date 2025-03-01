from math import sqrt, pow, cos, sin

class CoordinatesController:
    def __init__(self, odometry, drivebase):
        self.odometry = odometry
        self.drivebase = drivebase
        self.pid_x = PIDController(1.0, 0, 0)
        self.pid_y = PIDController(0.5, 0, 0)

    def move_to_coordinates(self, target_x: float, target_y: float, speed: float):
        self.odometry.reset_position(0, 0, 0)
        self.odometry.start_odometry()
        
        current_x = self.odometry.getPoseX()
        current_y = self.odometry.getPoseY()
        theta = self.odometry.getPoseTheta()
        
        distance = sqrt(pow((current_x - target_x), 2) + pow((current_y - target_y), 2))
        
        while distance > 2.1:
            current_x = self.odometry.getPoseX()
            current_y = self.odometry.getPoseY()
            theta = self.odometry.getPoseTheta()
            
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            deltaX = target_x - current_x
            deltaY = target_y - current_y
            
            error_x = cos_theta * deltaX + sin_theta * deltaY
            error_y = -sin_theta * deltaX + cos_theta * deltaY
            
            correction_x = self.pid_x.correction(error_x)
            correction_y = self.pid_y.correction(error_y)
            
            leftMotor = correction_x + correction_y
            RightMotor = correction_x - correction_y
            
            distance = sqrt(pow((current_x - target_x), 2) + pow((current_y - target_y), 2))
            self.drivebase.run_tank(leftMotor, RightMotor)
        
        self.drivebase.run_tank(0, 0)
