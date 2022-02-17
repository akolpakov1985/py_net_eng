# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

with open("E:\Projects\Python\pyneng\py_net_eng\exercises\\07_files\config_sw1.txt", 'r') as file:
    for line in file:
        #words = line.split()
        #flag = set(line.split()) & set(ignore)
        if not set(line.split()) & set(ignore) and not line.startswith("!"):
            print(line.rstrip())
