import socket
from threading import Thread
import os
import re
OPEN_PORTS = []
os.system("")


def validate_ip_address(address):
    match = re.match(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", address)

    if bool(match) is False:
        print("\033[91m {}\033[00m" .format("[-] IP address {} is not valid".format(address)))
        return False

    return True 

def scan_port(host, port):
  connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = connection.connect_ex((str(host), port))
  if result == 0:
    print("\033[92m {}\033[00m" .format("[+] Port " + str(port) + " is open"))
    OPEN_PORTS.append(str([port]))
  else:
    connection.close()

def scan_spec_ports(host, ports):
  for port in ports:
    scan_port(host,int(port))

def scan_seq_ports(host, AmountOfPorts):
  for port in range(1, AmountOfPorts+1):
    threads = []
    threads.append(Thread(target=scan_port, args=(host,port)))
    threads[-1].start()
  for thread in threads:
    thread.join()

def main():
  print("\033[91m {}\033[00m" .format('''
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓ ██░ ██  █    ██  ▄▄▄▄   
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓██░ ██▒ ██  ▓██▒▓█████▄ 
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒██▀▀██░▓██  ▒██░▒██▒ ▄██
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ░▓█ ░██ ▓▓█  ░██░▒██░█▀  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░    ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░     ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░ 
░░       ░ ░ ░ ▒    ░░   ░   ░       ░  ░░ ░ ░░░ ░ ░  ░    ░ 
             ░ ░     ░               ░  ░  ░   ░      ░      
                                                           ░ 
'''))
 
  host = input("\033[35m {}\033[00m" .format("[*] Enter The Host: "))
  while(validate_ip_address(host) == False):
    host = input("\033[35m {}\033[00m" .format("[*] Enter The Host: "))

  while True:
    
    Scan_Mode = input("\033[36m {}\033[00m" .format('''[*] Select Your Scan Type
 [*] 1: Specific Port(s) Scan
 [*] 2: Multi Port Scan
 --> '''))
    if Scan_Mode == '1' or Scan_Mode == '2':
      break

  if Scan_Mode=='1':
    user_input = input("\033[93m {}\033[00m" .format("[*] Which Port(s) Do You Want To Scan?\n [*] Syntex: 21,22,23\n "))
    ports = user_input.split(",")
    scan_spec_ports(host, ports)
  else:
    AmountOfPorts = int(input("\033[93m {}\033[00m" .format("[*] How Many Ports Do You Want To Scan?\n ")))
    scan_seq_ports(host, AmountOfPorts)
  print("\033[92m {}\033[00m" .format(OPEN_PORTS))


if __name__ == "__main__":
  main()