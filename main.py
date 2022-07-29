# This is a sample Python script.
import os
import xml.etree.ElementTree as ET


def print_separator():
    print('------------------------------------------')


def is_small_xml(fileName):
    result = False
    pattern = '.xml'
    large_size = 30000
    if fileName.endswith(pattern):
        file_stat = os.stat(fileName)
        if file_stat.st_size < large_size:
            result = True
    return result


def concatenate_of_files(list_xml):
    print(u'Начало объединения файлов')
    trees = []
    for file_xml in list_xml:
        trees.append(ET.parse(file_xml))
    new_file_name = input(u'Введите имя объединеного файла (без расширения) : ')
    new_file_name += ".xml"
    gtree = trees[0]
    groot = gtree.getroot()
    i = 1
    while i < len(trees):
        root = trees[i].getroot()
        for elem in root:
            groot.append(elem)
        i += 1
    gtree.write(new_file_name, encoding="utf-8")
    print(u'Файлы объединены в ' + f'{new_file_name}')


def delete_files(list_of_files):
    answer = input(u'Удалить обработанные файлы? y/n(н/т) ')
    if answer == 'y' or answer == 'Y' or answer == u'Н' or answer == u'н':
        for rmfile in list_of_files:
            os.remove(rmfile)
        print(u'Файлы удалены')
    else:
        print(u'Отказ удаления файлов')


if __name__ == '__main__':
    print(u'Сборка xml файлов для загрузки во ФГИС Аршин')
    print(u'Цель : уменьшить количество загружаемых файлов')
    print_separator()
    workDir = '.'
    listOfFiles = list(filter(is_small_xml, os.listdir(workDir)))
    print(u'Доступны файлы для обработки')
    for file in listOfFiles:
        print(file)
    lenOfFiles = len(listOfFiles)
    print(u'Всего файлов : ' + f'{lenOfFiles}')
    if lenOfFiles > 0:
        concatenate_of_files(listOfFiles)
        print_separator()
        delete_files(listOfFiles)
    else:
        print(u'Файлы для обработки отсутствуют')
    print_separator()
    print(u'Обработка закончена')
    input(u'Для закрытия окна нажмите Enter')


