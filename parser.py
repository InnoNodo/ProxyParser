import requests

file = open('proxies.txt', 'w')

print("Choose the type (socks4 | socks5 | http)")

while True:
    choice = input(f"Type your choice: ")
    if choice == 'socks4':
        response = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt')
        for line in response.text.splitlines():
            newLine = 'socks4://' + line + '\n'
            file.write(newLine)
        print("Your file is ready (proxies.txt)")
        break
    elif choice == 'socks5':
        response = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt')
        for line in response.text.splitlines():
            newLine = 'socks5://' + line + '\n'
            file.write(newLine)
        print("Your file is ready (proxies.txt)")
        break
    elif choice == 'http':
        response = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt')
        for line in response.text.splitlines():
            newLine = 'http://' + line + '\n'
            file.write(newLine)
        print("Your file is ready (proxies.txt)")
        break
    else:
        print("Try again")

