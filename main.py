import random
from os import path
import pyperclip


def get_properties():
    """"
    Functions that generates password
    """
    while True:
        characters_num = input('Enter the number of characters (8 - 24): ')
        if (int(characters_num) > 7) and (int(characters_num) < 25):
            break
    all_characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%'
    password = ''
    for i in range(int(characters_num)):
        password += random.choice(all_characters)
    return password


def is_exist(filename):
    """
    checks
    :param filename:
    :return: <Boolean> File exists in pdw
    """
    return path.exists(filename)


def write_file(password, username, webpage):
    """
    Writes password, username, webpage into a .txt file
    :param password: generated password
    :param username: username string
    :param webpage: webpage string
    :return: None
    """

    with open('passwords.txt', 'a') as file:
        file.write('====================\n')
        file.write(f"Webpage: {webpage}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write('====================\n')


def copy_to_clipboard(password):
    pyperclip.copy(password)
    return password


def new_data():
    yes = ['yes', 'yup', 'yea', '+1', 'yeah', 'tak', 'sure']
    webpage = input('Enter a webpage name: ')
    username = input('Enter your username: ')
    password = get_properties()
    write_file(password, username, webpage)
    print("Your data is in the file")
    print('-------------------------')
    user_copy_to_clipboard = input("Would you like copy your password to clipboard? (yes/no): ")
    if user_copy_to_clipboard.lower() in yes:
        copy_to_clipboard(password)
        print('Password copied successfully to your clipboard')


# main loop

def main():
    yes = ['yes', 'yup', 'yea', '+1', 'yeah', 'tak', 'sure']
    print("Hi user!")

    while True:
        print("-------------------")
        user_continue = input("Would you like to add new password? (yes/no): ")
        if user_continue.lower() in yes:
            new_data()
        else:
            print("So goodbye!")
            break


main()

