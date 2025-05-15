import paramiko
from getpass import getpass
import time

router1={
    'hostname': '172.16.37.1',
    'port': '22',
    'username': 'edcoronel',
    'password': 'I3tc@Emm@nu3l'
}
# host="ubuntu2.test.lab"
# username=(input(f'Enter username: ') or 'user1') #You have the option to set the default username
# password=getpass(f'Enter password: ')

#Interacting with SSH
session=paramiko.SSHClient()

#if you are getting SSHException. Use this command to bypass.
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# #to generate keys. initiate ssh using the terminal in the server(to verify use 'ssh-keygen -F <hostname>' or 'nano ~/.ssh/known_hosts').
# #If you want to read the hashed keys in ubuntu. Use this command 'nano /etc/ssh/ssh_config', then set HashKnownHosts to No
# #Using the generated key as a trusted key
# session.load_system_host_keys()                                                         #####you can use the exact file location by 'pwd' in the ~/.ssh directory.

# #If you want to reject the policy.
# session.set_missing_host_key_policy(paramiko.RejectPolicy())
# session.set_missing_host_key_policy(paramiko.WarningPolicy())

#Connecting to SSH using given creds.
session.connect(**router1, look_for_keys=False, allow_agent=False)

commands = ['show version\n']

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

