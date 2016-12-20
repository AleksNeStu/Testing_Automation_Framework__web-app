#INFO<br />

1) Selenium Builder 2,3 for Firefox:<br />

In order to enable ver.2 need to do in Firefox via "about:config":<br />

- Create:<br />
extensions.checkCompatibility.48.0.1 = false  *** 48.0.1 - version of Firefox<br />
extensions.checkUpdateSecurity = false<br />

- Modified:<br />
xpinstall.signatures.required = false<br />

2) Virtual env for project:<br />

virtualenv -p /usr/bin/python2.7 /pyweb<br />
chown -R ${USER:=$(/usr/bin/id -run)}:$USER /pyweb<br />
source /pyweb/bin/activate <br />
pip install -r ./tests/requirements.txt<br />
deactivate

Setting IDE (assign this virt env /pysel)

3) MySQL Connector:<br />

source /pyweb/bin/activate <br />
pip install http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.zip\#md5\=3df394d89300db95163f17c843ef49df<br />
deactivate<br />

*** https://pypi.python.org/pypi/mysql-connector-python/<br />


Addition info:
- Download the actual version of the connector from https://pypi.python.org/pypi/mysql-connector-python/:<br />
 *mysql-connector-python-2.0.4.zip<br />
- unzip it and install MySQL Connector/Python via shell><br />
 python ./setup.py install<br />

***Object-relational mapping (ORM, O/RM, and O/R mapping tool) in computer science is a programming technique for converting data between incompatible type systems in object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language.<br />




