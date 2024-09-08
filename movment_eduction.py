from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

movements = []

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

def record_movements():
    ev3.screen.print("Recording...")
    for _ in range(100):
        left_angle = left_motor.angle()
        right_angle = right_motor.angle()
        movements.append((left_angle, right_angle))
    ev3.screen.clear()
    ev3.screen.print("Recording stopped")

def replay_movements():
    ev3.screen.print("Replaying...")
    for left_angle, right_angle in movements:
        left_motor.run_target(100, left_angle, wait=False)
        right_motor.run_target(100, right_angle, wait=False)
    ev3.right_motor.clear()
    ev3.screen.print("Replay finished")
"""
FLL BLUE PHONIEX CODE !
"""
