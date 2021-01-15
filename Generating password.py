import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = lowercase_letters + uppercase_letters + punctuation + digits

length = int(input('Введите длину пароля: '))

def generate_password():
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

print(generate_password())