import paramiko
import os
import pickle

def send_angles_and_begin_drawing(angles):

   with open('angles.pkl', 'wb') as f:
      pickle.dump(angles, f)

   if (os.path.exists('angles.pkl')):
      print("FILE EXISTS")
   else:
         print("FILE DOES NOT EXIST")

   print(os.getcwd())


   host = "10.27.148.134" # Raspberry Pi IP address
   port = 22
   username = "pi"
   password = "robotics"

   ssh = paramiko.SSHClient() # Start the SSH client
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # This tells the package to automatically trust the ip address you tell it to connect to.
   ssh.connect(host, port, username, password) # Connect to the Raspberry Pi

   sftp_client=ssh.open_sftp() # SFTP clients allow us to perform secure file tranfer
   sftp_client.put('angles.pkl','/home/pi/Documents/FinalProject/angles.pkl') # NOTE: Need to add this folder to the Raspberry Pi
   sftp_client.close()

   # xhost + && export DISPLAY='10.27.148.134:0.0' && 

   ssh.exec_command("sudo killall pigpiod")
   stdin, stdout, stderr = ssh.exec_command("cd /home/pi/Documents/FinalProject/ && source /home/pi/miniconda3/bin/activate robotics3_env && python -V && sudo pigpiod && python -m DrawImage", get_pty=True)
   for line in iter(stdout.readline, ""):
      print(line, end="")
   print('finished.')

def send_draw_rectangle():

   host = "10.27.148.134" # Raspberry Pi IP address
   port = 22
   username = "pi"
   password = "robotics"

   ssh = paramiko.SSHClient() # Start the SSH client
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # This tells the package to automatically trust the ip address you tell it to connect to.
   ssh.connect(host, port, username, password) # Connect to the Raspberry Pi

   sftp_client=ssh.open_sftp() # SFTP clients allow us to perform secure file tranfer
   sftp_client.put('rectangle.pkl','/home/pi/Documents/FinalProject/rectangle.pkl') # NOTE: Need to add this folder to the Raspberry Pi
   sftp_client.close()

   # xhost + && export DISPLAY='10.27.148.134:0.0' && 

   ssh.exec_command("sudo killall pigpiod")
   stdin, stdout, stderr = ssh.exec_command("cd /home/pi/Documents/FinalProject/ && source /home/pi/miniconda3/bin/activate robotics3_env && python -V && sudo pigpiod && python -m DrawRectangle", get_pty=True)
   for line in iter(stdout.readline, ""):
      print(line, end="")
   print('finished.')


def send_erase():

   host = "10.27.148.134" # Raspberry Pi IP address
   port = 22
   username = "pi"
   password = "robotics"

   ssh = paramiko.SSHClient() # Start the SSH client
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # This tells the package to automatically trust the ip address you tell it to connect to.
   ssh.connect(host, port, username, password) # Connect to the Raspberry Pi

   sftp_client=ssh.open_sftp() # SFTP clients allow us to perform secure file tranfer
   sftp_client.put('erase.pkl','/home/pi/Documents/FinalProject/erase.pkl') # NOTE: Need to add this folder to the Raspberry Pi
   sftp_client.close()

   # xhost + && export DISPLAY='10.27.148.134:0.0' && 

   ssh.exec_command("sudo killall pigpiod")
   stdin, stdout, stderr = ssh.exec_command("cd /home/pi/Documents/FinalProject/ && source /home/pi/miniconda3/bin/activate robotics3_env && python -V && sudo pigpiod && python -m GoToErasePosition", get_pty=True)
   for line in iter(stdout.readline, ""):
      print(line, end="")
   print('finished.')


