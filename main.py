import socket

target = input('Enter website: ')
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print('INVALID WEBSITE ❌')
    exit()

print(f'SCANNING...{target} : {ip}....\n')

start = int(input('Enter starting port: '))
end   = int(input('Enter ending port: '))

found = False

for port in range(start,end+1):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((ip,port))

    if result == 0:
        print(f'\nport: {port} is OPEN 🔥')
        found = True

    sock.close()

if not found:
    print('\nno PORTS are OPEN...👋')


print('\n...SCAN complete ✅...\n')