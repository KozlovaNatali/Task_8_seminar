from data_create import name_data, surname_data, phone_data, address_data, number_records

def input_data():
    num_records = number_records()
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
        file.write(f'{num_records}. {name};{surname};{phone};{address}\n')


def print_data():

    print('Вывожу данные для Вас данные из Адресной книги:\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_second

def change_line(dataFile, numberRow, num_records):
    answer = input(f"Изменить данную запись\n{dataFile[numberRow]}?\nВведите ответ(да/нет): ")
    while answer != 'да':
        numberRow = int(input('Введите номер записи: ')) - 1

    print(f"Меняем данную запись\n{dataFile[numberRow]}\n")

    name = dataFile[numberRow].split(';')[0]
    surname = dataFile[numberRow].split(';')[1]
    phone = dataFile[numberRow].split(';')[2]
    address = dataFile[numberRow].split(';')[3]

    answer = int(input(f"Какие данные Вы хотите поменять?\n"
                       f"1. Имя\n"
                       f"2. Фамилия\n"
                       f"3. Номер телефона\n"
                       f"4. Адрес\n"
                       f"Введите ответ: "))
    while answer < 1 or answer > 4:
        print("Вы ошиблись!\nВведите корректный номер от 1 до 4")
        answer = int(input(f"Какие данные Вы хотите поменять?\n"
                           f"1. Имя\n"
                           f"2. Фамилия\n"
                           f"3. Номер телефона\n"
                           f"4. Адрес\n"
                           f"Введите ответ: "))
    if answer == 1:
        name = name_data()
    elif answer == 2:
        surname = surname_data()
    elif answer == 3:
        phone = phone_data()
    elif answer == 4:
        address = address_data()

    data_second = dataFile[:numberRow] + [f'{num_records}. {name};{surname};{phone};{address}'] + \
                    dataFile[numberRow + 1:]
    if numberRow + 1 == len(dataFile):
        data_second = dataFile[:numberRow] + [f'{num_records}.{name};{surname};{phone};{address}\n']
    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_second))
    print('Изменения успешно сохранены!')

def put_data():
    data_second = print_data()

    print("Какую именно запись по счету Вы хотите изменить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal -= 1
    change_line(data_second, number_journal, 2)


def delete_data():
    data_second = print_data()

    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    # Можно добавить проверку, чтобы человек не выходил за пределы записи
    print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
    data_second = data_second[:number_journal - 1] + data_second[number_journal:]
    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_second))
    print('Изменения успешно сохранены!')  # Можно вывести конечные данные
