#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# created by: ziwen.xu

import re
import subprocess
import platform
import socket


def make_hostname_ip():
    # 需要获取本机IP、绑定VIP和多网卡IP
    system=platform.system()
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    p=subprocess.Popen('ip a', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdout,errout) = p.communicate()
    if errout == 1:
        return None
    ip_pattern = re.compile('(inet %s)' % ipstr)
    if platform == "Linux":
        ip_pattern = re.compile('(inet addr:%s)' % ipstr)
    pattern = re.compile(ipstr)
    iplist = []
    for ipaddr in re.finditer(ip_pattern, str(stdout)):
        ip = pattern.search(ipaddr.group())
        if ip.group() != "127.0.0.1":
            iplist.append(ip.group())
    _hostname = socket.gethostname()
    iplist.append(_hostname)
    _iplist=str(iplist)
    # converst in str
    # _iplist.replace('[','(').replace(']',')')
    return _iplist.replace(_iplist[0],'(').replace(_iplist[-1],')')


def get_hostname_ip():
    #需要获取本机IP、绑定VIP和多网卡IP及hostname，兼容前端输入
    system=platform.system()
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    if system  == "Darwin" or system == "Linux":
        p=subprocess.Popen('ip a', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (stdout,errout) = p.communicate()
        if errout == 1:
            return None
        ip_pattern = re.compile('(inet %s)' % ipstr)
        if platform == "Linux":
            ip_pattern = re.compile('(inet addr:%s)' % ipstr)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, str(stdout)):
            ip = pattern.search(ipaddr.group())
            if ip.group() != "127.0.0.1":
                iplist.append(ip.group())

    elif system == "Windows":
        ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        ip_pattern = re.compile("IPv4 Address(\. )*: %s" % ipstr)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, str(output)):
            ip = pattern.search(ipaddr.group())
            if ip.group() != "127.0.0.1":
                iplist.append(ip.group())
    _hostname = socket.gethostname()
    iplist.append(_hostname)
    _iplist=str(iplist)
    # converst in str
    # _iplist.replace('[','(').replace(']',')')
    return _iplist.replace(_iplist[0],'(').replace(_iplist[-1],')')

print get_hostname_ip()
