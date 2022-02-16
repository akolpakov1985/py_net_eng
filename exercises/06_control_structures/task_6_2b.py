# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

flag = True
while flag:
    address = input("Введите адрес:")
    address_oct = address.split(".")
    valid_ip = len(address_oct) == 4

    for i in address_oct:
        valid_ip = i.isdigit() and int(i) in range(0, 256) and valid_ip

    if valid_ip:
        if 0 < int(address_oct[0]) < 224:
            print("unicast")
            break
        elif 223 < int(address_oct[0]) < 240:
            print("multicast")
            break
        elif address == "255.255.255.255":
            print("local broadcast")
            break
        elif address == "0.0.0.0":
            print("unassigned")
            break
        else:
            print("unused")
            break
    else:
        print(address, "- Неправильный IP-адрес")
