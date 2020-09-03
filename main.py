import random
from os import path


def get_properties():
    characters_num = input('Enter the number of characters (8 - 24): ')
    all_strings = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
    new_string = ''
    for i in range(int(characters_num)):
        new_string += random.choice(all_strings)
    print(new_string)
    return new_string


def is_exist(filename):
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


def main():
    print('Hello user!')
    webpage = input('Enter a webpage name: ')
    username = input('Enter your username: ')
    password = get_properties()
    write_file(password, username, webpage)
    print("Your passwords are into passwords.txt file")


main()


