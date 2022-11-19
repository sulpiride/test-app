def length_counter(num):
    return len(str(num))

def age_suffix(age):
    if 11 <= age % 100 <= 19:
        years_parameter = 'лет'
    elif age % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'
    return years_parameter

def general_info_user(name, age, phone, email, postcode, address, other_info):
    print(separator)
    print('Имя:    ', name)
    print('Возраст:', age, age_suffix(age))
    print('Телефон:', phone)
    print('E-mail: ', email)
    print('Индекс: ', postcode)
    print('Адрес:  ', address)
    if other_info:
        print('')
        print('Дополнительная информация:')
        print(other_info)


separator = '------------------------------------------'
# user profile
name = ''
age = 0
phone = ''
email = ''
postcode = ''
address = ''
other_info = ''
# business info
ogrnip = 0
inn = 0
bank_account = 0
cor_account = 0
bic = 0
bank_name = ''

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(separator)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break
    if option == 1:
        # submenu 1: edit info
        while True:
            print(separator)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while True:
                    # validate user age
                    a = int(input('Введите возраст: '))
                    if a > 0:
                        break
                    print('Возраст должен быть положительным')
                phone_input = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for sym in phone_input:
                    if sym == '+' or ('0' <= sym <= '9'):
                        phone += sym
                email = input('Введите адрес электронной почты: ')
                postcode_input = input('Введите индекс: ')
                postcode = ''
                for sym in postcode_input:
                    if '0' <= sym <= '9':
                        postcode += sym
                address = input('Введите адрес: ')
                other_info = input('Введите дополнительную информацию:\n')
            elif option2 == 2:
                # input business info
                while True:
                    ogrnip = int(input('Введите ОГРНИП: '))
                    if length_counter(ogrnip) == 15:
                        break
                    print('ОГРНИП должен содержать 15 цифр.')
                inn = int(input('Введите ИНН: '))
                while True:
                    bank_account = int(input('Введите номер счета: '))
                    if length_counter(bank_account) == 20:
                        break
                    print('Номер счета должен содержать 20 символов.')
                cor_account = int(input('Введите номер корреспондентского счета: '))
                bic = int(input('Введите БИК: '))
                bank_name = input('Введите название банка: ')
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(separator)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')
            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, postcode, address, other_info)
            elif option2 == 2:
                general_info_user(name, age, phone, email, postcode, address, other_info)
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:           ', ogrnip)
                print('ИНН:              ', inn)
                print('Номер счета:      ', bank_account)
                print('Номер кор. счета: ', cor_account)
                print('БИК:              ', bic)
                print('Название банка:   ', bank_name)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
