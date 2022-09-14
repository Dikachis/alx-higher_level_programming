# 0x0F. Python - Object-relational mapping
The goal of this project is to learn how to use an Object-relational mapper (ORM). The module MySQLdb will be used in Python to connect to a MySQL database, and then the module SQLAlchemy will be used.

# Learning Objectives
- To know why Python programming is awesome
- To know how to connect to a MySQL database from a Python script
- To know how to ``SELECT`` rows in a MySQL table from a Python script
- To know how to ``INSERT`` rows in a MySQL table from a Python script
- To know what ORM means
- To know how to map a Python Class to a MySQL table

## Background Context
- In this project, you will link two amazing worlds: Databases and Python!

- In the first part, you will use the module ``MySQLdb`` to connect to a MySQL database and execute your SQL queries.

- In the second part, you will use the module ``SQLAlchemy`` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

- The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

**Without ORM:**
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
**With an ORM:**
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## General Requirements
- Allowed editors: **vi**, **vim**, **emacs**
- All files are interpreted/compiled on Ubuntu 20.04 LTS using ``python3`` (version 3.8.5)
- Files were executed with ``MySQLdb`` version ``2.0.x``
- Files were executed with ``SQLAlchemy`` version ``1.4.x``
- All files ends with a new line
- The first line of all files were exactly ``#!/usr/bin/python3``
- code uses the pycodestyle (version ``2.8.*``)
- All files were executable
- All modules have a documentation (``python3 -c 'print(__import__("my_module").__doc__)'``)
- All classes have a documentation (``python3 -c 'print(__import__("my_module").MyClass.__doc__)'``)
- All functions (inside and outside a class) have a documentation (``python3 -c 'print(__import__("my_module").my_function.__doc__)'`` and ``python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'``)
- You are not allowed to use ``execute`` with sqlalchemy
- **Note:** A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Installation
**Install ``MySQLdb`` module version ``2.0.x``**
For installing ``MySQLdb``, you need to have ``MySQL`` installed:

- **How to install MySQL 8.0 in Ubuntu 20.04**
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
- **How to install MySQLdb module version 2.0.x in Ubuntu 20.04**
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```
- **How to install SQLAlchemy module version 1.4.x in Ubuntu 20.04**
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
Also, you can have this warning message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)
  ```
  You can ignore it.

### Resources
**Read or watch:**
- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial](https://mysqlclient.readthedocs.io/)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
- [Introduction to SQLAlchemy, **youtube**](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Flask SQLAlchemy, **youtube**](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
- [How To Install MySQL on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
- [How to Restart MySQL in Ubuntu](https://linuxhint.com/restart-mysql-in-ubuntu/)
- [MySQL - ERROR 1698 (28000) Access denied for user ‘root’@’localhost’](https://linuxnightly.com/error-1698-28000-access-denied-for-user-rootlocalhost/)

## Files & Description
Files | Description
----- | -----------
[0-select_states.py](./0-select_states.py) | Python script that lists all states from the database ``hbtn_0e_0_usa:``
[1-filter_states.py](./1-filter_states.py) | Python script that lists all ``states`` with a ``name`` starting with ``N`` (upper N) from the database ``hbtn_0e_0_usa:``
[2-my_filter_states.py](./2-my_filter_states.py) | Python script that takes in an argument and displays all values in the ``states`` table of ``hbtn_0e_0_usa`` where ``name`` matches the argument.
[3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | Python script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument safe from SQL injections
[4-cities_by_state.py](./4-cities_by_state.py) | Python script that lists all cities from the database hbtn_0e_4_usa
[5-filter_cities.py](./5-filter_cities.py) | Python script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
[model_state.py](./model_state.py) | python file that contains the class definition of a State and an instance Base = declarative_base()
[7-model_state_fetch_all.py](./7-model_state_fetch_all.py) | Python script that lists all State objects from the database hbtn_0e_6_usa
[8-model_state_fetch_first.py](./8-model_state_fetch_first.py) | Python script that prints the first State object from the database hbtn_0e_6_usa
[9-model_state_filter_a.py](./9-model_state_filter_a.py) | Python script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
[10-model_state_my_get.py](./10-model_state_my_get.py) | Python script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
[11-model_state_insert.py](./11-model_state_insert.py) | Python script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
[12-model_state_update_id_2.py](./12-model_state_update_id_2.py) | Python script that changes the name of a State object from the database hbtn_0e_6_usa
[13-model_state_delete_a.py](./13-model_state_delete_a.py) | Python script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
[model_city.py](./model_city.py) | Python file that contains the class definition of a City
[14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py) | Python script that prints all City objects from the database hbtn_0e_14_usa
