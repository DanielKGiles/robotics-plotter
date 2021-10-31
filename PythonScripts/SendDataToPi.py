import paramiko
import os
import pickle

def send_lines_and_begin_drawing(lines):

   with open('lines.pkl', 'wb') as f:
      pickle.dump(lines, f)

   if (os.path.exists('lines.pkl')):
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
   sftp_client.put('lines.pkl','/home/pi/Documents/BrachioGraph/lines.pkl') # NOTE: Need to add this folder to the Raspberry Pi
   sftp_client.close()

   # xhost + && export DISPLAY='10.27.148.134:0.0' && 

   stdin, stdout, stderr = ssh.exec_command("sudo killall pigpiod && cd /home/pi/Documents/BrachioGraph/ && source /home/pi/miniconda3/bin/activate robotics3_env && python -V && sudo pigpiod && python -m DrawImage.py", get_pty=True)
   for line in iter(stdout.readline, ""):
      print(line, end="")
   print('finished.')




