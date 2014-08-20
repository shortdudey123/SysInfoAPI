#!/usr/bin/env python
# =============================================================================
# file = filesystem.py
# description = Gets file system data
# author = GR <https://github.com/shortdudey123>
# create_date = 2014-07-29
# mod_date = 2014-07-29
# version = 0.1
# usage = 
# notes =
# python_ver = 2.7.6
# =============================================================================

import subprocess
import platform
import re

def getFilesystemData():
    retData = {}
    sys = platform.system()

    if sys == 'Linux':
        proc = subprocess.Popen(['df'], stdout=subprocess.PIPE)
        rawData = proc.communicate()
        rawData = rawData[0].replace('Mounted on', 'Mounted_on')
        rawDataLines = rawData.rstrip('\n').split('\n')

        # remove the header
        del rawDataLines[0]

        for line in rawDataLines:
            line = re.sub(' +', ' ', line)
            line = line.split(' ')

            retData[line[5]] = {'Filesystem': line[0],
                                '1K-blocks': line[1],
                                'Used': line[2],
                                'Available': line[3],
                                'UsePercent': line[4]
                               }

    elif sys == 'Darwin':
        proc = subprocess.Popen(['df'], stdout=subprocess.PIPE)
        rawData = proc.communicate()
        rawData = rawData[0].replace('Mounted on', 'Mounted_on')
        rawDataLines = rawData.rstrip('\n').split('\n')

        # remove the header
        del rawDataLines[0]

        for line in rawDataLines:
            print line
            line = line.replace('map -hosts', 'map_-hosts')
            line = line.replace('map auto_home', 'map_auto_home')
            print line

            line = re.sub(' +', ' ', line)
            line = line.split(' ')

            import pprint
            pprint.pprint(line)

            retData[line[8]] = {'Filesystem': line[0],
                                '512-blocks': line[1],
                                'Used': line[2],
                                'Available': line[3],
                                'UsePercent': line[4],
                                'iused': line[5],
                                'ifree': line[6],
                                'iusedPercent': line[7]
                               }

    return retData

if __name__ == '__main__':
    import pprint
    pprint.pprint(getFilesystemData())