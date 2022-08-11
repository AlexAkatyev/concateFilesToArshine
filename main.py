# This is a sample Python script.
import os
import xml.etree.ElementTree as ET


large_size = 2000000
max_size = 6000000


def print_separator():
    print('------------------------------------------')


def is_small_xml(fileName):
    result = False
    pattern = '.xml'
    if fileName.endswith(pattern):
        file_stat = os.stat(fileName)
        if file_stat.st_size < large_size:
            result = True
    return result


def get_new_name(file_name, counter):
    return file_name + "-" + f'{counter}' + ".xml"


def print_inc_and_del(file_xml, new_file_name, file_counter):
    print(u'Файл ' + f'{file_xml}' + u' включен в ' + get_new_name(new_file_name, file_counter) + u' и удален')


def concatenate_of_files(list_xml):
    new_file_name = input(u'Введите имя объединеного файла (без расширения) : ')
    file_counter = 1;
    print(u'Объединение файлов:')
    while len(list_xml) > 0:
        i = 0
        file_xml = list_xml[i]
        gtree = ET.parse(file_xml)
        groot = gtree.getroot()
        new_file_size = os.stat(file_xml).st_size
        os.remove(list_xml.pop(i))
        print_inc_and_del(file_xml, new_file_name, file_counter)
        while i < len(list_xml):
            file_xml = list_xml[i]
            add_size = os.stat(file_xml).st_size
            if new_file_size + add_size < max_size:
                new_file_size += add_size
                root = ET.parse(file_xml).getroot()
                for elem in root:
                    groot.append(elem)
                os.remove(list_xml.pop(i))
                print_inc_and_del(file_xml, new_file_name, file_counter)
            else:
                i += 1
        gtree.write(get_new_name(new_file_name, file_counter), encoding="utf-8")
        file_counter += 1


#  not in use
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
    else:
        print(u'Файлы для обработки отсутствуют')
    print_separator()
    print(u'Обработка закончена')
    input(u'Для закрытия окна нажмите Enter')


