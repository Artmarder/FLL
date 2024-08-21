from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

movements = []

def record_movements():
    ev3.screen.print("Recording...")
    for _ in range(100):
        left_angle = motor_left.angle()
        right_angle = motor_right.angle()
        movements.append((left_angle, right_angle))
        wait(100)
    ev3.screen.clear()
    ev3.screen.print("Recording stopped")

def replay_movements():
    ev3.screen.print("Replaying...")
    for left_angle, right_angle in movements:
        motor_left.run_target(100, left_angle, wait=False)
        motor_right.run_target(100, right_angle, wait=False)
        wait(100)
    ev3.screen.clear()
    ev3.screen.print("Replay finished")
"""
FLL BLUE PHONIEX CODE !
"""
