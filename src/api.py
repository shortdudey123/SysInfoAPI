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
import re

from filesystem import getFilesystemData

app = Flask(__name__)
api = restful.Api(app)

class sysInfo(restful.Resource):
    def get(self):
        sysData = createSysDict()
        return jsonify(sysData)

class sysInfoReq(restful.Resource):
    def get(self, sysReq):
        sysData = createSysDict()
        if sysReq in sysData.keys():
            return jsonify({sysReq:sysData[sysReq]})
        else:
            return not_found()

class pythonInfo(restful.Resource):
    def get(self):
        pythonData = createPythonDict()
        return jsonify(pythonData)

class pythonInfoReq(restful.Resource):
    def get(self, pythonReq):
        pythonData = createPythonDict()
        if pythonReq in pythonData.keys():
            return jsonify({pythonReq:pythonData[pythonReq]})
        else:
            return not_found()

class filesysInfo(restful.Resource):
    def get(self):
        filesysData = getFilesystemData()
        return jsonify(filesysData)

class filesysInfoReq(restful.Resource):
    def get(self, filesysReq):
        filesysData = getFilesystemData()
        filesysReqPath = re.sub('_', '/', filesysReq)
        if filesysReqPath in filesysData.keys():
            return jsonify({filesysReqPath:filesysData[filesysReqPath]})
        else:
            return not_found()

@app.route('/')
def index():
    sysData = createSysDict()
    pythonData = createPythonDict()
    filesysData = getFilesystemData()

    # remove / and replace with _ for api link
    filesysDataLink = {}
    for key in filesysData.keys():
        filesysDataLink[key] = re.sub('/', '_', filesysData)

    return render_template('index.html', sysData=sysData, pythonData=pythonData, filesysData=filesysData, filesysDataLink=filesysDataLink)

# based on http://blog.luisrei.com/articles/flaskrest.html
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404

    return response

def createSysDict():
    ret = {}
    ret['Platform'] = sys.platform
    ret['Arch'] = platform.architecture()
    ret['MachineType'] = platform.machine()
    ret['Name'] = platform.node()
    ret['Processor'] = platform.processor()
    ret['System'] = platform.system()
    ret['Release'] = platform.release()
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


def createPythonDict():
    ret = {}
    ret['Copyright'] = sys.copyright
    ret['Path'] = sys.path
    ret['Version'] = sys.version

    return ret

api.add_resource(sysInfo, '/api/1/SysInfo')
api.add_resource(sysInfoReq, '/api/1/SysInfo/<string:sysReq>')
api.add_resource(pythonInfo, '/api/1/PythonInfo')
api.add_resource(pythonInfoReq, '/api/1/PythonInfo/<string:pythonReq>')
api.add_resource(filesysInfo, '/api/1/FilesystemInfo')
api.add_resource(filesysInfoReq, '/api/1/FilesystemInfo/<string:filesysReq>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)