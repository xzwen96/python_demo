#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# created by: ziwen.xu

def get_disk_free():
    """
    获取本机最大空闲磁盘
    :return:
    """
    child = os.popen('df -lT')
    ret = child.read()
    err = child.close()
    if err:
        print '获取磁盘路径出错,df -lT failed with code %d'%err
        return '/data'
    statlines = ret.splitlines()
    stats = [line.split() for line in statlines]
    ret = []
    for index, value in enumerate(stats):
        if value[0] == 'Filesystem' or value[0] == 'none' or value[0] == 'udev' or value[0] == 'tmpfs':
            continue
        else:
            if len(value) == 1:
                lst = value + stats[index+1]
            else:
                lst = value
            if len(lst) == 7:
                ret.append(lst)
    result_dic={}
    for item in ret:
        result_dic[item[-1]]=item[-3]
    result_list=sorted(result_dic.items(), key=lambda d:d[1], reverse = True)
    return result_list[0][0]


print get_disk_free()
