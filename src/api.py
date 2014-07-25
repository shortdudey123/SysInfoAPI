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

from flask import Flask
from flask.ext import restful

import sys

app = Flask(__name__)
api = restful.Api(app)

class sysInfo(restful.Resource):
    def get(self):
        return {'hello': 'world'}

@app.route('/')
def index():
    return sys.platform

api.add_resource(sysInfo, '/api/1/sysInfo')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')