SysInfoAPI
==========

Installation
------------

Install virtualenv (if you have not already done so)

    sudo pip install virtualenv

Setup virtualenv and install the needed packages (start in the root dir of the repo)
    
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Run the server

    python src/api.py
    
Go to `http://<hostname>:5000/` in a web broswer to see what is available for your system

Testing
------------

This project has been tested on Unbuntu 14.04 and Mac OSX 10.9.4