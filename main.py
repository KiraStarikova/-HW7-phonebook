from importlib.resources import path
import interface as i
import input as inp
import output as out

defaultPath='data.csv'# дэфолтный справочник
dir='/-HW7-phonebook/'

def addPerson(path):
    while True:
        newline=inp.getLine()
        answer=input('Запись верна?\nЗаносить в справочник\n"a"-да, "r"-повторить, "q"-выйти: ')
        if answer=='a':
            print('Добавляю запись в файл...')
            inp.addToFile(path,newline)
            return
        if answer=='r':
            print('Повтрор...')
            continue
        if answer=='q':
            print('Выход...')
            return

while True:
    menu = i.main() #главное меню
    if menu == "1":
        subMenu = i.disp() # чтение из справочника
        if subMenu=="1":
            out.displayAllData(defaultPath)# вывод всего справочника
            continue
        if subMenu=="2":
            print('Ищу человека...')# пиоск человека
            print('НЕ ДОДЕЛАННО')
            continue
        elif subMenu=="r": #назад
            continue
        elif subMenu=="q": #выход
            break
        else:
            print("Некорректный ввод")
            break
    elif menu == "2":
        subMenu = i.imp()#запись в справочник
        if subMenu=="1": # добавить человека в справочник
            addPerson(defaultPath)
        elif subMenu=="r":  #назад
            continue
        elif subMenu=="q": #выход
            break
        else:
            print("Некорректный ввод")
            break
    elif menu == "3":
        subMenu = i.exp()#сщхранение в файл
        if subMenu=="1": # CVS
            target=out.saveToFile('.csv')
            print(f'сохраняю в {target}...')
            if target:
                out.exportToFile(defaultPath,target)
                continue
        if subMenu=="2": # JSON
            target=out.saveToFile('.json')
            print(f'сохраняю в {target}...')
            if target:
                out.exportToFile(defaultPath,target)
                continue
        if subMenu=="3": # XML
            target=out.saveToFile('.xml')
            print(f'сохраняю в {target}...')
            if target:
                out.exportToFile(defaultPath,target)
                continue
        elif subMenu=="r":  #назад
            continue
        elif subMenu=="q": #выход
            break
        else:
            print("Некорректный ввод")
            break
    elif menu=="q":
        break
    else:
        print("Некорректный ввод")
        continue

