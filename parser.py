import requests

file = open('proxies.txt', 'w')

while True:
    flag = input(f"Do you want to get prefix before the proxy? (y/n) ")
    if flag == 'y' or flag == 'yes':
        flag = 1
        break
    elif flag == 'n' or flag == 'no':
        flag=0
        break
    else:
        print("Choose correct option.")

print("Choose the type (socks4 | socks5 | http)")

while True:
    choice = input(f"Type your choice: ")
    if choice == 'socks4':
        response = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt')
        for line in response.text.splitlines():
            if flag: newLine = 'socks4://' + line + '\n'
            else: newLine = line + '\n'
            file.write(newLine)
        print("Your file is ready (proxies.txt)")
        break
    elif choice == 'socks5':
        response = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt')
        for line in response.text.splitlines():
            if flag: newLine = 'socks5://' + line + '\n'
            else: newLine = line + '\n'
            file.write(newLine)
        print("Your file is ready (proxies.txt)")
        break
    elif choice == 'http':
        response = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt')
        for line in response.text.splitlines():
            if flag: newLine = 'http://' + line + '\n'
            else: newLine = line + '\n'
            file.write(newLine)
        print("Your file is ready (proxies.txt)")
        break
    else:
        print("Try again")

