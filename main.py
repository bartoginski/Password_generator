import random
from os import path


def get_properties():
    """"
    Functions that generates password
    """
    while True:
        characters_num = input('Enter the number of characters (8 - 24): ')
        if (int(characters_num) > 7) and (int(characters_num) < 25):
            break
    all_characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
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


def main():
    """
    main function
    :return:
    """
    print('Hello user!')
    webpage = input('Enter a webpage name: ')
    username = input('Enter your username: ')
    password = get_properties()
    write_file(password, username, webpage)
    print("Your passwords are into passwords.txt file")


main()


