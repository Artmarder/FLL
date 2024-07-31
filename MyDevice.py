import micropython

from pybricks.ev3devices import Motor, GyroSensor

class Motor:
    """
    Represents a motor connected to the EV3.
    """

    def __init__(self, port):
        """
        Initializes a motor object.

        Args:
            port (str): The port where the motor is connected (e.g., 'A', 'B').
        """
        self.motor = Motor(port)
        self.position = 0

    def get_angle_position(self):
        """
        Returns the current angle position of the motor.

        Returns:
            int: The angle position in degrees.
        """
        return self.motor.angle()

    def get_rotations(self):
        """
        Returns the number of rotations completed by the motor.

        Returns:
            float: The number of rotations.
        """
        return self.motor.angle() / 360

    def get_speed(self):
        """
        Returns the current speed of the motor.

        Returns:
            int: The motor speed in degrees per second.
        """
        return self.motor.speed()

    def reset_position(self):
        """
        Resets the motor's position to zero.
        """
        self.motor.reset_angle(0)

class Gyro:
    """
    Represents a gyro sensor connected to the EV3.
    """

    def __init__(self, port):
        """
        Initializes a gyro sensor object.

        Args:
            port (str): The port where the gyro sensor is connected (e.g., 'S1', 'S2').
        """
        self.gyro = GyroSensor(port)

    def get_angle(self):
        """
        Returns the current angle measured by the gyro.

        Returns:
            float: The angle in degrees.
        """
        return self.gyro.angle()

    def get_speed(self):
        """
        Returns the current angular speed measured by the gyro.

        Returns:
            float: The angular speed in degrees per second.
        """
        return self.gyro.rate()

    def reset(self):
        """
        Resets the gyro sensor's angle to zero.
        """
        self.gyro.reset_angle(0)
