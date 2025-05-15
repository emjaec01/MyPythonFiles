import paramiko
from getpass import getpass
import time


host="ubuntu2.test.lab"
username=(input(f'Enter username: ') or 'user1') #You have the option to set the default username
password=getpass(f'Enter password: ')

#Interacting with SSH
session=paramiko.SSHClient()

#if you are getting SSHException. Use this command to bypass.
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Connecting to SSH using given creds.
session.connect(hostname=host, username=username, password=password)

#running a command
stdin, stdout, stderr = client.exec_command('hostname')
time.sleep(1)
print(f'The output of your command is: {stdout.read().decode()})

#closing the session
session.close()

