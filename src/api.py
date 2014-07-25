#!/usr/bin/env python
# =============================================================================
# file = api.py
# description = System Information API
# author = GR <https://github.com/shortdudey123>
# create_date = 2014-07-25
# mod_date = 2014-07-25
# version = 0.1
# usage = 
# notes =
# python_ver = 2.7.6
# =============================================================================

from flask import Flask, render_template, abort, redirect, url_for, request, jsonify
from flask.ext import restful

import sys
import platform
import time
import datetime

app = Flask(__name__)
api = restful.Api(app)

class sysInfo(restful.Resource):
    def get(self):
        sysData = createSysDict()
        return jsonify(sysData)

class sysInfoReq(restful.Resource):
    def get(self, sysReq):
        sysData = createSysDict()
        return jsonify({sysReq:sysData[sysReq]})

@app.route('/')
def index():
    sysData = createSysDict()
    return render_template('index.html', sysData=sysData)

def createSysDict():
    ret = {}
    ret['Platform'] = sys.platform
    ret['Arch'] = platform.architecture()
    ret['MachineType'] = platform.machine()
    ret['Name'] = platform.node()
    ret['Processor'] = platform.processor()
    ret['System'] = platform.system()
    ret['Release'] = platform.release()
    ret['Copyright'] = sys.copyright
    ret['Path'] = sys.path
    ret['Version'] = sys.version
    ret['Uname'] = platform.uname()

    # OS specific info
    if platform.system() == 'Linux':
        ret['Dist'] = platform.linux_distribution()
    elif platform.system() == 'Windows':
        ret['WinVer'] = sys.getwindowsversion()

    # time info
    ret['Time'] = time.time()
    ret['DateTime'] = datetime.datetime.now()

    return ret

api.add_resource(sysInfo, '/api/1/sysInfo')
api.add_resource(sysInfoReq, '/api/1/sysInfo/<string:sysReq>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)