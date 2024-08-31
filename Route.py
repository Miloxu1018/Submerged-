from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
front_motor = Motor(Port.F)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
robot.use_gyro(True)
hub = PrimeHub()
SPEED = 150
ACCEL = 700
TURN_RATE = 150
TURN_ACCEL = 1750
ANGLE = 45
STRAIGHT = 200
BACKWARD = -100
FSENSTIVILITY = 2
MOTOR_ANGEL = 400
BACKWARD_MOTOR = -55
MOTOR_SPEED = 250
SECONED_SPEED = 500
robot.settings(SPEED, ACCEL, TURN_RATE, TURN_ACCEL)
robot.straight(STRAIGHT)
wait(1000)
front_motor.run_angle(MOTOR_SPEED,MOTOR_ANGEL, then=Stop.HOLD, wait=False)
wait(1000)
robot.turn(ANGLE)
wait(1000)
robot.straight(-100)
front_motor.run_angle(SECONED_SPEED,-MOTOR_ANGEL, then=Stop.BRAKE)

