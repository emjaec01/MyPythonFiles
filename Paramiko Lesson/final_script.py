from csv import DictReader
import paramiko
import time

from Scripts.unicodedata import lookup

conf_dict={}
with open('02_config_in_column.csv', 'r') as csv_file:
    csv_content=DictReader(csv_file)
    column_names=csv_content.fieldnames
    # print(column_names)
    for row in csv_content:
        for column_name in column_names:
            if not column_name:
                continue
            if not row[column_name]:
                continue
            if column_name not in conf_dict.keys():
                conf_dict[column_name]= []
            conf_dict[column_name].append(row[column_name])
session=paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for ip in conf_dict.keys():
    try:
        print(f'Connecting to {ip}...')
        session.connect(hostname=ip, username='admin', password='pass')
        DEVICE_ACCESS=session.invoke_shell()
        print(f'Executing commands are \n{conf_dict[ip]}')
        for conf in conf_dict[ip]:
            DEVICE_ACCESS.send(conf+ '\n')
            time.sleep(3)
            output=DEVICE_ACCESS.recv(65000)
            print(output.decode(), end="")
            time.sleep(5)
        session.close()
    except:
        print(f'Cannot connect to the device...')
print(f'{'*'*30}\n Command execution completed \n {'*'*30}')


