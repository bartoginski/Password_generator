import random


def get_properties():
    characters_num = input('Enter the number of characters (8 - 24): ')
    all_strings = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
    new_string = ''
    for i in range(int(characters_num)):
        new_string += random.choice(all_strings)
    print(new_string)


# Password generator
# with open('some_file.txt', 'w') as file:
#     file.write('Password Generator!\n')
#     file.write('====================\n')
#     file.write('\n')



get_properties()


# >>> import string
# >>> string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# >>> import random
# >>> random.choice(string.ascii_letters)
# 'j'