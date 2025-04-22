import os
from time import sleep
from tkinter import *
import tkinter as tk
from colorama import Fore
from validations import (
    read_parameters,
    validate_password,
    password_wordslist,
    check_password_complexity,
    check_repeated_characters,
    check_palindrome,
    choose_file
)

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