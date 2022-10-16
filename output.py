import os
import csv
import json

def displayAllData(path):
    file=open(path,'r',encoding='utf-8')
    print("Содержимое справочника (",path,"):")
    print('-'*43)
    counter=0
    for line in file:
        print(counter,line.replace(',','| '), end='')
        counter+=1
    file.close()

def findPerson(path,nubmer):
    file=open(path,'r',encoding='utf-8')
    counter=0
    for line in file:
        if counter==nubmer:#пока так
            person=",".join(line.split('\n'))
        counter+=1
    file.close()
    return person

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

def exportToFile(fromFile,toFile):# дефолтная сохранялка
    source=open(fromFile,'r',encoding="utf-8")
    with open(toFile,'w',encoding="utf-8") as target:
            for line in source:
                target.write(line)
    source.close()

def lineCountInFile(path):
    file=open(path,'r',encoding="utf-8")
    lines=0
    for line in file:
        if line != "\n":
            lines+=1
    file.close()
    return lines

def showPerson(path):
    count=lineCountInFile(path)
    while True:
        print(f'В файле {count-1} записей,')
        answer=input(' какую вывести? ')
        if answer.isdigit():
            if (1<=int(answer)<=count-1):
                print('Вывожу...')
                displayPerson(findPerson(path,int(answer)))#тут допилить исключения? 
                return
        else:
            print("Некорректный ввод")
        continue

def exportToJson(sourse,target):
    with open(sourse, encoding="utf-8") as CSV, \
            open(target, "w", encoding="utf-8") as JSON:
        dic = {}
        reader = csv.DictReader(CSV)
        for line in reader:
            key = line['Surname']
            dic[key] = line        
        JSON.write(json.dumps(dic, indent=2))


# sourse = 'data.csv'
# target='data.xml'

def printXml(headers, line):
    result = f'<person id="{line[0]}">\n'
    for header, item in zip(headers, line):
        result += f'    <{header}>' + f'{item}' + f'</{header}>\n'
    return result + '</row>'

def exportToXml(sourse,target):
    with open(sourse, 'r', encoding="utf-8") as CSV, \
        open(target, "w", encoding="utf-8") as XML:
        reader = csv.reader(CSV)
        headers = next(reader)
        XML.write('<data>\n')
        for line in reader:
            XML.write(printXml(headers, line) + '\n')
        XML.write('</data>')


#exportToXml(sourse,target)