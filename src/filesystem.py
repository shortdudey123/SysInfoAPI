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

def getFilesystemData():
    retData = {}
    sys = platform.system()

    if sys == 'Linux':
        proc = subprocess.Popen(["df"], stdout=subprocess.PIPE)
        rawData = proc.communitcat()
        rawDataLines = rawData.split('\n')
        print rawDataLines
    return retData

if __name__ == '__main__':
    getFilesystemData()