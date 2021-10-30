import paramiko
import os
import pickle

def send_lines_and_begin_drawing(lines):
    # os.system('ssh pi@{}')
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

   # command0 = 'ls'
   # stdin, stdout, stderr = ssh.exec_command(command0) # Run the above command on the Raspberry Pi
   # output = stdout.readlines() # Get the output from the Raspberry Pi's command line and print the result in the current terminal
   # print(output)

   sftp_client=ssh.open_sftp() # SFTP clients allow us to perform secure file tranfer
   sftp_client.put('lines.pkl','/home/pi/Documents/BrachioGraph/lines.pkl') # NOTE: Need to add this folder to the Raspberry Pi
   sftp_client.close()

   command1 = "cd /home/pi/Documents/BrachioGraph/"
   command2 = "python DrawImage.py" # When run, this command will run the DrawImage.py file on the Raspberry Pi

   stdin, stdout, stderr = ssh.exec_command(command1) # Run the above command on the Raspberry Pi
   output = stdout.readlines() # Get the output from the Raspberry Pi's command line and print the result in the current terminal
   print(output)

   stdin, stdout, stderr = ssh.exec_command(command2) # Run the above command on the Raspberry Pi
   output = stdout.readlines() # Get the output from the Raspberry Pi's command line and print the result in the current terminal
   print(output)


