from csv import DictReader
import paramiko
import time

for ip in conf_dict.keys():
    print(f'IP address is {ip}')
    for conf in conf_dict[ip]:
        print(conf)


