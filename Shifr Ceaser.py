side = input('h = шифрование или d = дешифрование?  ')
language = input('ru = russian or en = english? ')
step = int(input('Какой шаг? '))
eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

text = input('Введи текст для шифрования: ')
result = ''
if language == 'ru' and side == 'h':
    for i in text:
        if i == ' ':
            result += ' '
            continue
        elif i == ',':
            result += ','
            continue
        elif i == '!':
            result += '!'
            break
        elif i == '?':
            result += '?'
            break
        elif i == '.':
            result += '.'
            break
        else:
            if i.isupper():
                num = rus_upper_alphabet.find(i) + step
                if int(num) >= len(rus_upper_alphabet):
                    num -= len(rus_upper_alphabet)
                    result += rus_upper_alphabet[num]
                else:
                    result += rus_upper_alphabet[num]
            else:
                num = rus_lower_alphabet.find(i) + step
                if int(num) >= len(rus_lower_alphabet):
                    num -= len(rus_lower_alphabet)
                    result += rus_lower_alphabet[num]
                else:
                    result += rus_lower_alphabet[num]
elif language == 'en' and side == 'h':
    for i in text:
        if i == ' ':
            result += ' '
            continue
        elif i == ',':
            result += ','
            continue
        elif i == '!':
            result += '!'
            break
        elif i == '?':
            result += '?'
            break
        elif i == '.':
            result += '.'
            break
        else:
            if i.isupper():
                num = eng_upper_alphabet.find(i) + step
                if int(num) >= len(eng_upper_alphabet):
                    num -= len(eng_upper_alphabet)
                    result += eng_upper_alphabet[num]
                else:
                    result += eng_upper_alphabet[num]
            else:
                num = eng_lower_alphabet.find(i) + step
                if int(num) >= len(eng_lower_alphabet):
                    num -= len(eng_lower_alphabet)
                    result += eng_lower_alphabet[num]
                else:
                    result += eng_lower_alphabet[num]
elif language == 'en' and side == 'd':
    for i in text:
        if i == ' ':
            result += ' '
            continue
        elif i == ',':
            result += ','
            continue
        elif i == '!':
            result += '!'
            break
        elif i == '?':
            result += '?'
            break
        elif i == '.':
            result += '.'
            break
        else:
            if i.isupper():
                num = eng_upper_alphabet.find(i) - step
                if int(num) < 0:
                    num += len(eng_upper_alphabet)
                    result += eng_upper_alphabet[num]
                else:
                    result += eng_upper_alphabet[num]
            else:
                num = eng_lower_alphabet.find(i) - step
                if int(num) < 0:
                    num += len(eng_lower_alphabet)
                    result += eng_lower_alphabet[num]
                else:
                    result += eng_lower_alphabet[num]
else:
    for i in text:
        if i == ' ':
            result += ' '
            continue
        elif i == ',':
            result += ','
            continue
        elif i == '!':
            result += '!'
            break
        elif i == '?':
            result += '?'
            break
        elif i == '.':
            result += '.'
            break
        else:
            if i.isupper():
                num = rus_upper_alphabet.find(i) - step
                if int(num) < 0:
                    num += len(rus_upper_alphabet)
                    result += rus_upper_alphabet[num]
                else:
                    result += rus_upper_alphabet[num]
            else:
                num = rus_lower_alphabet.find(i) - step
                if int(num) < 0:
                    num += len(rus_lower_alphabet)
                    result += rus_lower_alphabet[num]
                else:
                    result += rus_lower_alphabet[num]
print(result)