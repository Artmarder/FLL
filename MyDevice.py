import micropython

class PortError(Exception):
    def __init__(self, port):
        self.port = port

class Motor:

    """
    in this class we confrig the motor.
    """
    
    def __init__(self, config: object, **kwargs):
        self.motorA = LargeMotor('A')
        self.motorB = LargeMotor('B')
   
    def get_angel_postioin_A():
    positionA = self.motorA.position
    return positionA

    def get_angel_postioin_B():
        positionB = self.motorB.position
        return positionB

    def getRotA():
        Rot = positionA / 360
        return Rot
        
    def getRotB():
        Rot = positionB / 360
        return Rot

    

    def SpeedMotorA():
        speedMotorA = motor.speed
        return speedMotorA
        
    def SpeedMotorB():
        speedMotorB = motor.speed
        return speedMotorB


    def ResetPostionA():
        global positionA
        positionA = 0
        return position

    def ResetPostionB():
        global positionA
        positionB = 0
        return position

    def calcDistance():
        correct_postionA = get_angel_postioin_A()
        correct_postionB = get_angel_postioin_B()
        calc_distance =correct_postionB  + correct_postionA  / 360 / 2 * 17.5


class Gyro :

    def GetAngel():
        getAngel =  gyro_sensor.angle
        return getAngel

    def GetSpeed():
        GyroSpeed = gyro_sensor.rate
        return GyroSpeed
    
    def ResetGyro():
        Reset = reset_angle()
        return Reset

    








    
