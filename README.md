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

Note: you may need to update iptables if it is running (update 127.0.0.1 to your IP or remove it entirely
)

	sudo iptables -I INPUT 1 -p tcp -s 127.0.0.1 --dport 5000 -j ACCEPT

Testing
------------

This project has been tested on Unbuntu 14.04 and Mac OSX 10.9.4