import os
from time import sleep

'''
* Function to read the password and its length requirements from a file.
* The first line of the file should contain the password.
* The second line should contain the minimum length.
* The third line should contain the maximum length.
* The function returns the password, minimum length, and maximum length.
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
* Function to validate the password length based on the given minimum and maximum length.
* The function returns True if the password length is valid, otherwise False.
'''
def validate_password(password, min_length, max_length):
    if min_length <= len(password) <= max_length:
        return True
    else:
        return False

def password_wordslist(password, file_path_rockyou):
    with open(file_path_rockyou, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        common_passwords = [line.strip() for line in lines[3:]]
    if password in common_passwords:
        return True
    else:
        return False

'''
* Function to check the complexity of the password based on the following criteria:
* 1. Length: At least 8 characters.
* 2. Contains at least one digit.
* 3. Contains at least one uppercase letter.
* 4. Contains at least one lowercase letter.
* 5. Contains at least one special character.
* The function returns a message indicating the complexity level of the password.
'''
def check_password_complexity(password):
    count_complexity = 0
    conditions = [
        (len(password) > 8, "Password is too short."),
        (any(char.isdigit() for char in password), "The password does not contain digits."),
        (any(char.isupper() for char in password), "The password does not contain uppercase letters."),
        (any(char.islower() for char in password), "The password does not contain lowercase letters."),
        (any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for char in password),
         "The password does not contain special characters.")
    ]

    for condition, message in conditions:
        if condition:
            count_complexity += 1
        else:
            print(message)
    if count_complexity == 1:
        return "The password is weak."
    elif count_complexity == 2:
        return "The password is medium."
    elif count_complexity == 3:
        return "The password is strong."
    elif count_complexity == 4:
        return "The password is very strong."
    elif count_complexity == 5:
        return "The password is extremely strong."
    else:
        return "The password does not meet any complexity requirements."

'''
* Main function to execute the password validation program.
'''
def main():
    file_path_rockyou = os.path.join(os.path.dirname(__file__), 'rockyou.txt')
    file_path_input = input("Enter the file path: ")
    if not os.path.exists(file_path_input):
        print(f"File does NOT exist: {file_path_input}")
    else:
        print(f"File FOUND: {file_path_input}")
    try:

        print("Checking if password is valid...")
        password, min_length, max_length = read_parameters(file_path_input)
        sleep(3)
        if validate_password(password, min_length, max_length):
            print("The password length is valid.")
        else:
            print("The password length is invalid.")

        print("Checking if password is common...")
        common_password = password_wordslist(password, file_path_rockyou) # Check if the password is in the common passwords list
        sleep(3)
        if common_password:
            print("The password is common.")
        else:
            print("The password is not common.")

        print("Checking the complexity of the password...")
        sleep(3)
        print(check_password_complexity(password))

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()