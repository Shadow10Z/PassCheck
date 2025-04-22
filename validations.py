from colorama import Fore
from tkinter import filedialog

'''
---------------------------------------------------------------------------
* Function to read the password and its length requirements from a file.
* The first line of the file should contain the password.
* The second line should contain the minimum length.
* The third line should contain the maximum length.
* The function @returns the password, minimum length, and maximum length.
---------------------------------------------------------------------------
'''
def read_parameters(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Raw file lines: {lines}")
        if len(lines) < 3:
            raise ValueError("The file does not have the requirements.")
        password = lines[0].strip()
        min_length = int(lines[1].strip())
        max_length = int(lines[2].strip())
    return password, min_length, max_length

'''
---------------------------------------------------------------------------
* Function to validate the password length based on the given minimum and maximum length.
* The function @returns True if the password length is valid, otherwise False.
---------------------------------------------------------------------------
'''
def validate_password(password, min_length, max_length):
    if min_length <= len(password) <= max_length:
        return Fore.GREEN + "The password length is valid."
    else:
        return Fore.RED + "The password length is invalid."

'''
---------------------------------------------------------------------------
* Function to check if the password is in the common passwords list (rockyou.txt).
---------------------------------------------------------------------------
'''
def password_wordslist(password, file_path_rockyou):
    with open(file_path_rockyou, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        common_passwords = [line.strip() for line in lines[3:]]
    if password in common_passwords:
        return Fore.RED + "The password is common."
    else:
        return Fore.GREEN + "The password is not common."

'''
---------------------------------------------------------------------------
* Function to check the complexity of the password based on the following criteria:
* 1. Length: At least 8 characters.
* 2. Contains at least one digit.
* 3. Contains at least one uppercase letter.
* 4. Contains at least one lowercase letter.
* 5. Contains at least one special character.
* The function @returns a message indicating the complexity level of the password.
---------------------------------------------------------------------------
'''
def check_password_complexity(password):
    count_complexity = 0
    conditions = [
        (len(password) > 8, Fore.YELLOW + "Password is too short."),
        (any(char.isdigit() for char in password), Fore.YELLOW + "The password does not contain digits."),
        (any(char.isupper() for char in password), Fore.YELLOW + "The password does not contain uppercase letters."),
        (any(char.islower() for char in password), Fore.YELLOW + "The password does not contain lowercase letters."),
        (any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for char in password),
         Fore.YELLOW + "The password does not contain special characters.")
    ]

    for condition, message in conditions:
        if condition:
            count_complexity += 1
        else:
            print(message)
    if count_complexity == 1:
        return Fore.LIGHTRED_EX + "The password is weak."
    elif count_complexity == 2:
        return Fore.LIGHTYELLOW_EX + "The password is medium."
    elif count_complexity == 3:
        return Fore.LIGHTGREEN_EX + "The password is strong."
    elif count_complexity == 4:
        return Fore.GREEN + "The password is very strong."
    elif count_complexity == 5:
        return Fore.MAGENTA + "The password is extremely strong."
    else:
        return Fore.RED + "The password does not meet any complexity requirements."

'''
---------------------------------------------------------------------------
* Function to check if the password contains too many repeated characters.
---------------------------------------------------------------------------
'''
def check_repeated_characters(password, max_repeats=4):
    count = 1
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            count += 1
            if count >= max_repeats:
                return Fore.RED + "Password contains too many repeated characters."
        else:
            count = 1

    return Fore.GREEN + "Password does not contain too many repeated characters."

'''
---------------------------------------------------------------------------
* Function to check if the password is a palindrome.
---------------------------------------------------------------------------
'''
def check_palindrome(password):
    if password == password[::-1]:
        return Fore.RED + "Password is a palindrome."
    else:
        return Fore.GREEN + "Password is not a palindrome."

'''
---------------------------------------------------------------------------
* Function to open a file dialog and select a file.
---------------------------------------------------------------------------
'''
def choose_file():
    filetypes = [("Text files", "*.txt"), ("All files", "*.*")]
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=filetypes)
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected.")
    return file_path