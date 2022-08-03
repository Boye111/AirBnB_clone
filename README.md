# The AirBnB clone project
# Description
This project included:
# CMD
This is a support for line command interpreters. The cmd class provides a simple framework for writing line oriented command interpreters. These are often useful for test harnessess, administrative tools, and prototypes that will later be wrapped in a more sophisticated interface.
# UUID Object
This module provide immutable UUID objects(the uuid class) and the functions uuid1(), uuid3(), uuid4(), uuid5() for generating version 1,3,4, and 5 uuids.
# Datetime
The datetime module supplies classes for manipulating dates and time
category
# Aware
# Naive.
# Unittest
# Method for implementing the AirBnB clone project
Put in place a BaseModel which serves as the Parent Class.
BaseModel take care of the initialization, serialization and deserialization of your future instances.
# Classes for AirBnB include:
User, State, City, Place all from the BaseModel
# Abstracted storage for the project
create unittests to validate all our classes and storage engine
# Files description
AUTHORS file has a list of individuals that contributed content to the repository.
console.py file contains a command line interpreter limited to a specific use-case. for this project manage the objects of our project using this console.

models folder contains all the Class modules of the project, and a folder called engine.
tests folder contains all the UNITTEST of every module stored in the models folder and the TEST of the console.py file.
# Features
Programming language: python3
Style: All modules use the PEP 8 style
Documentation: All modules have documentation, including the functions, classes,etc.
# Usage
The console (console.py) works like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  destroy  show  all  update

(hbnb)
(hbnb)
(hbnb) quit
$
But also in non-interactive mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  destroy  show  all  update
$
# Authors
Ubochi Luggard Uzochukwu
github username
luggardubochi.
Adeboye Akingbelure
github username
Boye111
