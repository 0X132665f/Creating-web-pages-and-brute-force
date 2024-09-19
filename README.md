# Project Overview

This project utilizes HTML, Python, CSS, and JavaScript.

## Installation

First, install the necessary Python libraries by running the following commands in your terminal:

```bash
pip install colorama
pip install requests
pip install flask
pip install flask-cors
```

### Brute Force Principle and Dictionary Attack

#### Brute Force Principle
The brute force principle involves systematically trying every possible combination of characters to guess a password or decrypt a message. This method is exhaustive and time-consuming, but it guarantees finding the correct solution if given enough time and computational power.

#### Dictionary Attack
A dictionary attack is a more efficient form of brute force attack. Instead of trying every possible combination, it uses a precompiled list of likely passwords (a "dictionary") to attempt to gain unauthorized access. This method is faster than a pure brute force attack because it targets common passwords and phrases.

## Usage

1. Run the `index.html` and `app.py` files.
2. Set the  `password` in your `app.py` files.
3. Set the `url` variable in the `bruteforce_csv.py` file to the URL you want to target.
4. Set the `username` variable to the username you want to target.
5. Set the `password_file` variable to the path of the downloaded `passwords.csv` file.
6. Execute the `bruteforce_csv.py` file to attempt the attack.

**Note:** This project is for educational purposes only. Unauthorized access to computer systems is illegal and unethical.
