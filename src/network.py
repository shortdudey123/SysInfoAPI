#!/usr/bin/env python
# =============================================================================
# file = network.py
# description = Gets file system data
# author = GR <https://github.com/shortdudey123>
# create_date = 2014-08-28
# mod_date = 2014-08-28
# version = 0.1
# usage = 
# notes =
# python_ver = 2.7.6
# =============================================================================

import netifaces

def getNetworkData():
    retData = {}

    for interface in netifaces.interfaces():
        retData[interface] = netifaces.ifaddresses(interface)

    retData['__GATEWAY__'] = netifaces.gateways()

    return retData

def getNetworkDataInt(interface):
    retData = {}

    if interface in netifaces.interfaces():
        retData = netifaces.ifaddresses(interface)
    elif interface == '__GATEWAY__':
        retData = netifaces.gateways()

    return retData

def getNetworkDataIntType(interface, networkDataType):
    retData = {}

    if interface in netifaces.interfaces():
        if networkDataType == 'ipv4' and netifaces.AF_INET in netifaces.ifaddresses(interface).keys():
            retData = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
        elif networkDataType == 'ipv6' and netifaces.AF_INET6 in netifaces.ifaddresses(interface).keys():
            retData = netifaces.ifaddresses(interface)[netifaces.AF_INET6][0]
        elif networkDataType == 'link' and netifaces.AF_LINK in netifaces.ifaddresses(interface).keys():
            retData = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
    elif interface == '__GATEWAY__':
        if networkDataType == 'ipv4':
            retData = netifaces.gateways()[netifaces.AF_INET][0]
        elif networkDataType == 'ipv6':
            retData = netifaces.gateways()[netifaces.AF_INET6][0]

    return retData

if __name__ == '__main__':
    import pprint
    pprint.pprint(getFilesystemData())