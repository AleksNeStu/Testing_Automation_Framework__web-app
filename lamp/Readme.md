#INFO

1) Credites:
http://127.0.0.1/addressbook/index.php
admin
secret

http://127.0.0.1/index.php
user
bitnami

2) Database:
mysql -u root -h 172.18.0.2
CREATE DATABASE test;
mysql -u root -h 172.18.0.2 test < addressbook.sql
http://lamp/addressbook/diag.php
config/cfg.db.php » according to your providers information.
 $dbname = "test"; 
 $dbserver = ""; 
 $dbuser = "root"; 
 $dbpass = "";
 
3) IP:
172.18.0.3 lamp (web-app)
172.18.0.2 mysql
172.18.0.1 bridge (host)

4) Selenium server:
https://hub.docker.com/r/selenium/standalone-firefox/
How to use this image
docker run -d -P selenium/standalone-firefox
You can acquire the port that Selenium is listening on by running:
docker port <container-name|container-id> 4444 => 0.0.0.0:49338

5) Chmod:
chmod -R a+w /www/joomla/administrator/cache
chmod -R a+w /www/joomla/cache

#RUN

docker-compose up