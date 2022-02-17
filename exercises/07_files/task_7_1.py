# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

template = '''
Prefix                {0}
AD/Metric             {1}
Next-Hop              {2}
Last update           {3}
Outbound Interface    {4}
'''

with open("E:\Projects\Python\pyneng\py_net_eng\exercises\\07_files\ospf.txt", 'r') as ospf_route:
    for line in ospf_route:
        ospf_out = line[8:].replace(",", " ").strip().replace("  ", " ").split(" ")
        print(template.format(ospf_out[0], ospf_out[1][1:-1], ospf_out[3], ospf_out[4], ospf_out[5]))


#print(template.format(ospf_out[0], ospf_out[1][1:-1], ospf_out[3], ospf_out[4], ospf_out[5]))