import paramiko
from getpass import getpass
import time

hostname='192.168.229.11'
username='admin'
password='pass'

cmd=["enable",
     "pass",
     "terminal length 0",
     "show running",
     "show version"]
#Interacting with SSH
session=paramiko.SSHClient()

#if you are getting SSHException. Use this command to bypass.
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Connecting to SSH using given creds.
session.connect(hostname=hostname, username=username, password=password, allow_agent=False, look_for_keys=False)
shell= session.invoke_shell()
for command in cmd:
    shell.send(f'{command}\n')
    time.sleep(1)
    output=shell.recv(65000)
    print(output.decode(), end= "")

if session.get_transport().is_active() == True:
    print('Closing the connection.')
    session.close()

