#!/usr/bin/env pybricks-micropython
from PID import PIDController
from driveBsae import Drivebase

drivebase = Drivebase()
class MrRobot:
    def __init__(self, drivebase):
        self.PIDController = PIDController(7, 0, 0)
        self.drivebase = drivebase

    def PIDDriveForward(self, speed: float, distance: float, setPoint: float, KP,KI,KD):
        self.drivebase.resetMotors(0, 0)
        self.drivebase.resetGyro(0)
        pid = PIDController(KP, KI, KD)

        while self.drivebase.getDistance() < distance:
            current_angle = self.drivebase.getGyro()

            error = setPoint - current_angle
            if error < -180:
                error += 360
            correction = pid.correction(error)
            if error == 0:
                correction == 0
            print(correction,"corection")
            print(error,"error")
            print(current_angle,"current angle")
            
            self.drivebase.run_tank(speed + correction, speed - correction)
        self.drivebase.run_tank(0, 0)


    def PIDDriveBack(self, speed: float, distance: float, setPoint: float, KP,KI,KD):
        pid = PIDController(KP, KI, KD)

        while self.drivebase.getDistance() > distance:
            current_angle = self.drivebase.getGyro()

            error = setPoint - current_angle
            if error < -180:
                error += 360
            correction = pid.correction(error)
            print(correction,"corection")
            print(error,"error")
            print(current_angle,"current angle")
            
            self.drivebase.run_tank(speed + correction, speed - correction)
        self.drivebase.run_tank(0, 0)

    def Turn(self, angel: float, KP,KI,KD):
        self.drivebase.resetMotors(0, 0)
        self.drivebase.resetGyro(0)
        pid = PIDController(KP, KI, KD)

        current_angle = self.drivebase.getGyro()

        error = angel - current_angle
            
        while error <= -2.1 or error >=2.1:
            current_angle = self.drivebase.getGyro()
            if current_angle is None:
                current_angle = self.drivebase.getGyro()
            error = angel - current_angle
            

            correction = pid.correction(error)
            print(correction, "correction")
            print(error, "error")
            print(current_angle,"current angle")
            self.drivebase.run_tank(-correction * 0.8, correction*0.8)
        self.drivebase.run_tank(0, 0)




    
    def TurnMinus(self, angel: float, KP,KI,KD):
        self.drivebase.resetMotors(0, 0)
        self.drivebase.resetGyro(0)
        pid = PIDController(5, 0.11,0.4)

        current_angle = self.drivebase.getGyro()

        if current_angle is None:
            current_angle = 0
        error = angel - current_angle
        if error < -180:
            error += 360
            
        while error <= -2.1 or error >=2.1:
            current_angle = self.drivebase.getGyro()
            if current_angle is None:
                current_angle = self.drivebase.getGyro()
            error = angel - current_angle
            if error < -180:
                error += 360
            

            correction = pid.correction(error)
            print(correction, "correction")
            print(error, "error")
            print(current_angle,"current angle")
            self.drivebase.run_tank(correction, -correction)
        self.drivebase.run_tank(0, 0)

    def forwardMotor1(self,Speed,Degrees):  
        pid = PIDController(1, 0, 0)

        Current_Speed_Motor = self.drivebase.motorspeed1()
        error = Speed - Current_Speed_Motor
        while self.drivebase.AngleMotor1() < Degrees:
            correction = pid.correction(error)
            self.drivebase.run_motor1(Speed + correction)
        self.drivebase.run_motor1(0)
    
    def forwardMotor2(self,Speed,Degrees):
        pid = PIDController(1, 0, 0)

        Current_Speed_Motor = self.drivebase.motorspeed2()
        error = Speed - Current_Speed_Motor
        while self.drivebase.AngleMotor2() < Degrees:
            correction = pid.correction(error)
            self.drivebase.run_motor2(Speed + correction)
        self.drivebase.run_motor2(0)



    def backMotor1(self,Speed,Degrees):
        pid = PIDController(1, 0, 0)
        Current_Speed_Motor = self.drivebase.motorspeed1()
        error = Speed - Current_Speed_Motor
        while self.drivebase.AngleMotor1() > Degrees:
            correction = pid.correction(error)
            self.drivebase.run_motor1(Speed + correction)
        self.drivebase.run_motor1(0)


    def backMotor2(self,Speed,Degrees): 
        pid = PIDController(1, 0, 0)
        Current_Speed_Motor = self.drivebase.motorspeed2()
        error = Speed - Current_Speed_Motor
        while self.drivebase.AngleMotor2() > Degrees:
            correction = pid.correction(error)
            self.drivebase.run_motor2(Speed + correction)
        self.drivebase.run_motor2(0)
    
    def Run_Tank_Motors_samll(self,vell,degrees):
        self.drivebase.resetMotors(0, 0)
        pid = PIDController(1, 0.011,0)

        averg_degrees =  self.drivebase.AngleMotor2()
        while averg_degrees < degrees:
            averg_degrees = (self.drivebase.AngleMotor1() + self.drivebase.AngleMotor2()) / 2
            error1 = vell - self.drivebase.motorspeed1()
            error2 = vell - self.drivebase.motorspeed2()
            correction1 = pid.correction(error1)
            correction2 = pid.correction(error2)
            self.drivebase.run_motor1(vell + correction1)
            self.drivebase.run_motor2(-(vell + correction2))
            print(averg_degrees)
        self.drivebase.run_motor1(0)
        self.drivebase.run_motor2(0)
