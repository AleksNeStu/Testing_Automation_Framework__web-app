# Testing automation framework for web-app "Address book"<br />
# Technologies stack: docker, pytest, python, selenium<br />

# [Open test-cases](https://github.com/AleksNeStu/Test_Automation_Framework_WEB-APP/tree/master/tests/test) <br />

# Structure:<br />
/add - pre-requirements
/lamp - test web-app (lamp) and selenium under docker images (containers)<br />
/framework - testing automation framework<br />
/framework/test - tests (test's methods) under pytest framework<br />

# URLs:<br />
http://127.0.0.1:4444/wd/hub - selenium server<br />
http://127.0.0.1:80/index.php (443) - CMS joomla<br />
http://127.0.0.1:80/addressbook/index.php - test web-app<br />

# Quick start:<br />
/lamp/run_lamp.sh - build (firstly) and run (usual) docker containers with web-app instance