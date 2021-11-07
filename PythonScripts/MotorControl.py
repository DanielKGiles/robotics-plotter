import pickle
import turtle
# from typing import _get_type_hints_obj_allowed_types
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

class MotorController:

   def __init__(self):
      pigpio_factory = PiGPIOFactory()
      self.left_servo = AngularServo(14, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=pigpio_factory)  
      self.right_servo = AngularServo(15, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=pigpio_factory)  
      self.up_down_servo = AngularServo(18, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=pigpio_factory)  
      self.go_to_default_positions()

   def go_to_default_positions(self):
      self.left_servo.angle = 0
      self.right_servo.angle = 0
      self.up_down_servo.angle = -75

   def go_to_angle(self, angle, motor):
      if motor == "left":
         self.left_servo.angle = angle
      elif motor == "right":
         self.right_servo.angle = angle

   def pen_up(self):
      self.up_down_servo.angle = -50

   def pen_down(self):
      self.up_down_servo.angle = -75

   def angles_to_pwm(self, servo, angle):
      servo.angle = angle

   def plot_file(self, filename='angles.pkl'):
      pickle_file = open(filename,"rb")
      objects = []
      while True:
         try:
            objects.append(pickle.load(pickle_file))
         except EOFError:
            break

      pickle_file.close()
      angles = objects[0]

      self.plot_angles(angles)

   def plot_angles(self, angles, wait=1.31):
      for i, line in enumerate(angles):

         # Lift up pen, go to the beginning of each line, then put the pen down
         self.pen_up()
         self.angles_to_pwm(self.left_servo, angles[i][0][0])
         self.angles_to_pwm(self.right_servo, angles[i][0][1])
         self.pen_down()
         sleep(wait) # Time for the motors to reach their new positions

         for j, angle in enumerate(line):
            
            self.angles_to_pwm(self.left_servo, angle[0])
            self.angles_to_pwm(self.right_servo, angle[1])
            sleep(wait) # Time for the motors to reach their new positions
      

      