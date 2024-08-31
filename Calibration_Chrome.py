from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
front_motor = Motor(Port.F)
MOTOR_ANGEL = -400
MOTOR_SPEED = 250
front_motor.run_angle(MOTOR_SPEED, MOTOR_ANGEL, then=Stop.HOLD)