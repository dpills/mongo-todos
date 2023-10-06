# MongoDB Quick Start Guide

This respository shows a simple example of how to use CRUD (Create, Read, Update, Delete) operations with Python and MongoDB.
The python packages are managed with [Poetry](https://python-poetry.org/).

## Setup

```bash
$ docker-compose up -d
[+] Building 0.0s (0/0)                                                                                                                                docker-container:unruffled_shockley
[+] Running 2/0
 ✔ Network mongo_todos_default      Created   
 ✔ Volume "mongo_todos_my_db_data"  Created   
 ⠋ Container myDataBase             Creating 

$ poetry install
Installing dependencies from lock file

$ poetry shell
Spawning shell within...
```

## Usage

```bash
$ python3 todos.py --help
usage: todos.py [-h] [-o {create,read,complete,delete}] [-d DATA]

Mongo CRUD Operations

options:
  -h, --help            show this help message and exit
  -o {create,read,complete,delete}, --operation {create,read,complete,delete}
                        Choose CRUD Operation
  -d DATA, --data DATA  New ToDo or ID of existing ToDo
```
