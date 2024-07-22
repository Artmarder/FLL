import micropython

class PortError(Exception):
    def __init__(self, port):
        self.port = port

class Motor:
    """
    in this class we confrig the motor.
    """
    
    def __init__(self, config: object, **kwargs):

        self._port = micropython.const(config.port)

        if not self.connected():
            raise PortError(self._port)


        
    def get_angel_postioin():
    position = motor.position
    return position

    def getRot():
        Rot = position / 360
        return Rot

    def SpeedMotor():
        speedMotor = motor.speed
        return speedMotor

    def ResetPostion():
        global position
        position = 0
        return position


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

    








    
