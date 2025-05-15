import paramiko
from getpass import getpass
import time

hostname='192.168.229.11'
username='admin'
password='pass'
# host="ubuntu2.test.lab"
# username=(input(f'Enter username: ') or 'user1') #You have the option to set the default username
# password=getpass(f'Enter password: ')

#Interacting with SSH
session=paramiko.SSHClient()

#if you are getting SSHException. Use this command to bypass.
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Connecting to SSH using given creds.
print(f'Connecting to {username}....')
session.connect(hostname=hostname, username=username, password=password, allow_agent=False, look_for_keys=False)

commands = ['enable','conf t','hostname AutomationSW']

for command in commands:
    print(f'Executing the commands...')
    #running a command
    stdin, stdout, stderr = session.exec_command(command)
    time.sleep(1)
    print(stdout.read().decode())
    err=stderr.read().decode()
    if err:
        print(err)

#closing the session
session.close()

