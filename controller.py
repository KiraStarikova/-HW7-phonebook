import interface as i
import input as inp
import output as out
import os

defaultPath='data.csv'# дэфолтный справочник

def checkPath(pathToCheck):# дефолтная проверка пути
    if os.path.exists(pathToCheck):
        return pathToCheck
    print('Файл не найден', end=', ')
    return inp.getPath()

def menu():
    while True:
        menu = i.main() #главное меню
        if menu == "1":
            subMenu = i.disp() # чтение из справочника
            if subMenu=="1":
                currentPath=checkPath(defaultPath)
                if currentPath=='q':
                    print('Пропуск...')
                    continue
                else:
                    out.displayAllData(currentPath)# вывод всего справочника
                    continue
            if subMenu=="2":
                print('Ищу человека...')# пиоск человека
                currentPath=checkPath(defaultPath)
                if currentPath=='q':
                    print('Пропуск...')
                    continue
                else:
                    out.showPerson(currentPath)
                    continue
            elif subMenu=="r": #назад
                continue
            elif subMenu=="q": #выход
                break
            else:
                print("Некорректный ввод")
                continue
        elif menu == "2":
            subMenu = i.imp()#запись в справочник
            if subMenu=="1": # добавить человека в справочник
                currentPath=checkPath(defaultPath)
                if currentPath=='q':
                    print('Пропуск...')
                    continue
                else:
                    inp.addPerson(currentPath)
                    continue
            elif subMenu=="r":  #назад
                continue
            elif subMenu=="q": #выход
                break
            else:
                print("Некорректный ввод")
                continue
        elif menu == "3":
            currentPath=checkPath(defaultPath)
            if currentPath=='q':
                    print('Пропуск...')
                    continue
            else:
                subMenu = i.exp()#сщхранение в файл
                if subMenu=="1": # CVS
                    target=out.saveToFile('.csv')
                    print(f'сохраняю в {target}...')
                    if target:
                        out.exportToFile(currentPath,target)
                        continue
                if subMenu=="2": # JSON
                    target=out.saveToFile('.json')
                    print(f'сохраняю в {target}...')
                    if target:
                        out.exportToJson(currentPath,target)
                        continue
                if subMenu=="3": # XML
                    target=out.saveToFile('.xml')
                    print(f'сохраняю в {target}...')
                    if target:
                        out.exportToXml(currentPath,target)
                        continue
                elif subMenu=="r":  #назад
                    continue
                elif subMenu=="q": #выход
                    break
                else:
                    print("Некорректный ввод")
                    continue
        elif menu=="q":
            break
        else:
            print("Некорректный ввод")
            continue

