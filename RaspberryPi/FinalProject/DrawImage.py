from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

from MotorControl import *

motor_controller = MotorController()
print("Beginning Plotting")
motor_controller.plot_file(filename="angles.pkl")

# from time import sleep
# motor_controller.angles_to_pwm(motor_controller.left_servo, 90)
# motor_controller.angles_to_pwm(motor_controller.right_servo, 90)
# sleep(2)
# motor_controller.angles_to_pwm(motor_controller.left_servo, -90)
# motor_controller.angles_to_pwm(motor_controller.right_servo, -90)

# from time import sleep
# motor_controller.go_to_angle(0,"left")
# sleep(2)
# motor_controller.go_to_angle(20,"left")
# sleep(2)
# motor_controller.go_to_angle(45,"left")
# sleep(2)
# motor_controller.go_to_angle(65,"left")
# sleep(2)
# motor_controller.go_to_angle(90,"left")
# sleep(2)
# motor_controller.go_to_angle(0,"left")
#  sleep(2)
# motor_controller.go_to_angle(-90,"left")
# sleep(2)
# motor_controller.go_to_angle(-90,"left")
# sleep(2)
# motor_controller.go_to_angle(90,"left")
# sleep(2)
# motor_controller.go_to_angle(-90,"left")
# motor_controller.go_to_angle(10,"left")
# sleep(2)
# motor_controller.go_to_angle(80,"left")
# motor_controller.go_to_angle(70,"right")

############################################################
# TEST

# from time import sleep
# from gpiozero import AngularServo
# from gpiozero.pins.pigpio import PiGPIOFactory
# pigpio_factory=PiGPIOFactory()
# servo = AngularServo(14, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=pigpio_factory)
# servo.angle = 0
# sleep(2)
# servo.angle = 45

############################################################

print("THE WHOLE THING WORKED!!!!!")