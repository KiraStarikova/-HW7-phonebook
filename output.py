import os

def displayAllData(path):
    file=open(path,'r',encoding='utf-8')
    print("Содержимое справочника (",path,"):")
    print('-'*43)
    counter=0
    for line in file:
        print(counter,line.replace(',','| '), end='')
        counter+=1
    file.close()

def displayPerson(person):
    lst=person.split(',')
    print('-'*20)
    print(f'Фамилия: {lst[0]}\nИмя:     {lst[1]}\nОтчество: {lst[2]}\nТелефон: {lst[3]}\nЗаметка: {lst[4]}')
    print('-'*20)

def saveToFile(ext):
    while True:
        file=input('Имя файла:')
        if not os.path.exists(file+ext):
            return file+ext
        print('Уже есть такой файл')
        return ''

def exportToFile(fromFile,toFile):
    source=open(fromFile,'r',encoding="utf-8")
    with open(toFile,'w',encoding="utf-8") as target:
            for line in source:
                target.write(line)
    source.close()