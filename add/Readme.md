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



