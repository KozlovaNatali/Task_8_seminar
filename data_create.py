def number_records():
    with open('data_second_variant.csv', 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        num_records = len(lines)
    return (num_records + 1)
    
def name_data():
    name = input('Введите Ваше имя: ')
    print('Очень красивое имя! (а меня зовут гб_бот, меня создала компания GeekBrains!')
    return name


def surname_data():
    surname = input('Введите Вашу фамилию: ')
    return surname


def phone_data():
    # import re
    phone = input('Введите Ваш телефон: ')
    return phone


def address_data():
    address = input('Введите Ваш адрес: ')
    return address
