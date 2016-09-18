#INFO<br />

1) Credites:<br />
http://127.0.0.1/addressbook/index.php<br />
admin<br />
secret<br />

http://127.0.0.1/index.php<br />
user<br />
bitnami<br />

2) Database:<br />
mysql -u root -h 172.18.0.2<br />
MariaDB [(none)]> CREATE DATABASE test;<br />
MariaDB [(none)]> exit;
mysql -u root -h 172.18.0.2 test < addressbook.sql<br />
http://lamp/addressbook/diag.php<br />
config/cfg.db.php » according to your providers information.<br />
 $dbname = "test"; <br />
 $dbserver = "172.18.0.2"; <br />
 $dbuser = "root"; <br />
 $dbpass = "";<br />
 
3) IP:<br />
172.18.0.1 bridge (host)<br />
172.18.0.2 mysql<br />
172.18.0.3 lamp (web-app)<br />
172.18.0.4 selenium-server (firefox)<br />

4) Selenium server:<br />
https://hub.docker.com/r/selenium/standalone-firefox/<br />
How to use this image<br />
docker run -d -P selenium/standalone-firefox<br />
You can acquire the port that Selenium is listening on by running:<br />
docker port <container-name|container-id> 4444 => 0.0.0.0:49338<br />

5) Chmod:<br />
chmod -R a+w /www/joomla/administrator/cache<br />
chmod -R a+w /www/joomla/cache<br />

#RUN<br />

docker-compose up<br />


#FIX TROUBLES<br />
Recreate containers if have some problems to fix them:<br />

docker-compose up -d --force-recreate mariadb<br />
docker-compose up -d --force-recreate application<br />
docker-compose up -d --force-recreate selenium<br />
docker-compose up -d --force-recreate *** for  all<br />