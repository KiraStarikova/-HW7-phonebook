import os
def addToFile(path,newline):
    with open(path,'a',encoding='utf-8') as file:
        if isInFile(path,newline):
            print(chr(10060)*3+' Есть такая запись '+chr(10060)*3)
            return
        print(chr(9989)*3+' Запись добавлена '+chr(9989)*3)
        file.write('\n'+newline)

def isInFile(path,newline):
    file=open(path,'r',encoding='utf-8')
    for line in file.readlines():
        if line==newline:
            return True
    file.close()
    return False

def getLine():
    while True:
        name=input('Имя: ')
        if name.isalpha() and name.istitle():
            break
    while True:   
        surname=input('Фамилия: ')
        if surname.isalpha() and surname.istitle():
            break
    while True:
        patronymic=input('Отчество: ')
        if patronymic.isalpha() and patronymic.istitle():
            break
    while True:
        phone=input('Телефон: ')
        if phone.isdigit():
            break
    note=input('Заметка: ')
    return surname+','+name+','+patronymic+','+phone+','+note

def getPath():
    path=''
    while not os.path.exists(path):
        path=input('введите имя файла ')
    return path

def addPerson(path):# это в input
    while True:
        newline=getLine()
        answer=input('Запись верна?\nЗаносить в справочник\n"a"-да, "r"-повторить, "q"-выйти: ')
        if answer=='a':
            print('Добавляю запись в файл...')
            addToFile(path,newline)
            return
        if answer=='r':
            print('Повтрор...')
            continue
        if answer=='q':
            print('Выход...')
            return
