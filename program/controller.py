import view
import json

dict_contact = {}
contacts =list(dict_contact.keys())
parametr = ["Phone number", "Email"]


def start():
    while True:
        op = view.operations()
        if op == 1:
            while True:
                name = view.add_contact()
                if name not in list(dict_contact.keys()):
                    dict_contact[name] = {}
                    contacts.append(name)
                    if parametr:
                        for pole in parametr:
                            dict_contact[name][pole] = []
                print('-' * 20)
                exit = input('Нажмите 1, если хотите еще добавить контакт \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    with open("teldir.json", "w") as fl:
                        json.dump(dict_contact, fl)
                    break

        elif op ==2:
            while True:
                pole=view.add_pol()
                parametr.append(pole)
                for k in dict_contact:
                    dict_contact[k][pole]=[]
                print('-' * 20)
                exit = input('Нажмите 1, если хотите еще добавить поле для информации  \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    with open("teldir.json", "w") as fl:
                        json.dump(dict_contact, fl)
                    break

        elif op == 3:
            while True:
                print('Перед вами представлен список контактов: ')
                for k, name in enumerate(contacts, 1):
                    print(k, name)
                # for key in dict_contact:
                #     print(key)
                print('Перед вами представлен список полей для заполнения информации: ')
                for k, less in enumerate(parametr, 1):
                    print(k, less)
                print('-'*20)
                view.add_info_contact(dict_contact)
                print('-' * 20)
                exit = input('Нажмите 1, если хотите еще заполнить информацию \n'
                           'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit =='1':
                    continue
                elif exit == '0':
                    with open("teldir.json", "w") as fl:
                        json.dump(dict_contact, fl)
                    break

        elif op == 4:
            while True:
                for k, name in enumerate(contacts, 1):
                    print(k, name)
                # for key in dict_contact:
                #     print(key)
                print('-' * 20)
                exit = input('Нажмите 0, чтобы вернуться в главное меню \n')
                if exit == '0':
                    break

        elif op == 5:
            while True:
                view.out_info_contact2(dict_contact)
                print('-' * 20)
                exit = input('Нажмите 1, если хотите посмотреть информацию о других контактах \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    break
        elif op == 6:
            while True:
                view.delete_contact(dict_contact, contacts)
                print('-'*20)
                exit = input('Нажмите 1, если хотите удалить еще один контакт \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    with open("teldir.json", "w") as fl:
                        json.dump(dict_contact, fl)
                    break

        elif op == 7:
            while True:
                print('Перед вами представлен список контактов: ')
                for k, name in enumerate(contacts, 1):
                    print(k, name)
                print('Перед вами представлен список полей для изменения информации: ')
                for k, less in enumerate(parametr, 1):
                    print(k, less)
                print('-' * 20)
                view.change_info_contact(dict_contact)
                print('-' * 20)
                exit = input('Нажмите 1, если хотите еще изменить  информацию \n'
                             'Нажмите 0, если хотите вернуться в главное меню \n')
                if exit == '1':
                    continue
                elif exit == '0':
                    with open("teldir.json", "w") as fl:
                        json.dump(dict_contact, fl)
                    break

        elif op == 8:
            while True:
                with open('D:/pythonProject/telefdir23/teldir.json') as fl:
                    dict_new_contact = json.load(fl)
                dict_contact.update(dict_new_contact)
                contacts_2= list(dict_contact.keys())
                contacts.extend(contacts_2)
                print('-' * 20)
                exit = input('Нажмите 0, чтобы вернуться в главное меню \n')
                if exit == '0':
                    break


        elif op == 9:
            print('   До свидания!')
            break