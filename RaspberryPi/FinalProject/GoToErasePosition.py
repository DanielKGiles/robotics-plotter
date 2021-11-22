from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

from MotorControl import *

motor_controller = MotorController()
motor_controller.plot_file(filename="erase.pkl")
print("Moving to erase position complete")