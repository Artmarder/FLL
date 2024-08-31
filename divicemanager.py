from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import Button, Port
from pybricks.hubs import EV3Brick
from time import ticks_ms, ticks_diff, sleep

WHEEL_CIRCUMFERENCE = 17.5

motorL = Motor(Port.A)
motorR = Motor(Port.B)

motorLUP = Motor(Port.D)
motorRUP = Motor(Port.F)

current_angleL = motorL.angle()
current_angleR = motorR.angle()

current_angleLUP = motorLUP.angle()
current_angleRUP = motorRUP.angle()


class GyroSensorManager:
    def __init__(self):
        self.gyro_sensor = GyroSensor(Port.S1)


class MotorManager:
    def __init__(self, exit_exec):
        self.motor_a = Motor(Port.A)
        self.motor_b = Motor(Port.B)
        self.exit_exec = exit_exec

    def check_exit(self):
        return self.exit_exec()


class ColorSensorManager:
    def __init__(self):
        self.color_sensor_left = ColorSensor(Port.S1)
        self.color_sensor_right = ColorSensor(Port.S2)


class DeviceManager:
    def __init__(self):
        pass


class Parameters:
    def __init__(self):
        self.speed = 100



def calculate_distance():
    left_distance = current_angleL * WHEEL_CIRCUMFERENCE / 360
    right_distance = current_angleR * WHEEL_CIRCUMFERENCE / 360
    return (left_distance + right_distance) / 2


def calculate_speedLUP():
    interval = 100
    initial_angle = current_angleLUP
    initial_time = ticks_ms()

    sleep(interval / 1000)

    final_angle = motorLUP.angle()
    final_time = ticks_ms()

    angle_change = final_angle - initial_angle
    time_change = ticks_diff(final_time, initial_time)

    if time_change == 0:
        return 0

    speed = angle_change / (time_change / 1000)

    return speed


def calculate_speedRUP():
    interval = 100
    initial_angle = current_angleRUP
    initial_time = ticks_ms()

    sleep(interval / 1000)

    final_angle = motorRUP.angle()
    final_time = ticks_ms()

    angle_change = final_angle - initial_angle
    time_change = ticks_diff(final_time, initial_time)

    if time_change == 0:
        return 0

    speed = angle_change / (time_change / 1000)

    return speed


def calculate_speedL():
    interval = 100
    initial_angle = current_angleL
    initial_time = ticks_ms()

    sleep(interval / 1000)

    final_angle = motorL.angle()
    final_time = ticks_ms()

    angle_change = final_angle - initial_angle
    time_change = ticks_diff(final_time, initial_time)

    if time_change == 0:
        return 0

    speed = angle_change / (time_change / 1000)

    return speed


def calculate_speedR():
    interval = 100
    initial_angle = current_angleR
    initial_time = ticks_ms()

    sleep(interval / 1000)

    final_angle = motorR.angle()
    final_time = ticks_ms()

    angle_change = final_angle - initial_angle
    time_change = ticks_diff(final_time, initial_time)

    if time_change == 0:
        return 0

    speed = angle_change / (time_change / 1000)

    return speed


robot = Robot()
