import os
from time import sleep
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from colorama import Fore

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

'''
---------------------------------------------------------------------------
* Main function to execute the password validation program.
---------------------------------------------------------------------------
'''
def main():
    try:

        window = Tk()
        window.geometry("400x300")
        window.title("Password Checker")
        window.configure(bg="#2E3B4E")

        #icon = PhotoImage(file="logo.jpg")
        #window.iconphoto(True, icon)

        lbl = tk.Label(
            window,
            text="Check how strong is your password",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#2E3B4E",
            padx=20,
            pady=10
        )
        lbl.grid(column=0, row=0, padx=10, pady=20)

        #window.withdraw()

        def process_file():
            file_path_input = choose_file()
            if file_path_input:
                file_path_rockyou = os.path.join(os.path.dirname(__file__), 'rockyou.txt')
                if not os.path.exists(file_path_input):
                    print(f"File does NOT exist: {file_path_input}")
                else:
                    print(f"File FOUND: {file_path_input}")

                # Checks if the content in the file is valid
                print(Fore.CYAN + "Checking if password is valid...")
                password, min_length, max_length = read_parameters(file_path_input)

                # First Verification
                print(Fore.CYAN + "Checking the length of the password...")
                sleep(3)
                print(validate_password(password, min_length, max_length))

                # Second Verification
                print(Fore.CYAN + "Checking if password is common...")
                sleep(3)
                print(password_wordslist(password, file_path_rockyou))

                # Third Verification
                print(Fore.CYAN + "Checking the complexity of the password...")
                sleep(3)
                print(check_password_complexity(password))

                # Fourth Verification
                print(Fore.CYAN + "Checking for repeated characters...")
                sleep(3)
                print(check_repeated_characters(password))

                # Fifth Verification
                print(Fore.CYAN + "Checking if password is a palindrome...")
                sleep(3)
                print(check_palindrome(password))

        btn = tk.Button(
            window,
            text="Choose File",
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
            activebackground="#45A049",
            activeforeground="white",
            padx=10,
            pady=5,
            relief="groove",
            borderwidth=3,
            command=process_file
        )
        btn.grid(column=0, row=1, padx=10, pady=20)

        window.mainloop()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()