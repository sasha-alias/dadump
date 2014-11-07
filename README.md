dadump
======

Daily dumps management for Postgresql

Creates a directory structure:

    destination/yyyy-mm-dd/dbname.dump

Handles several databases in parallel.
Removes old dumps according to retention configuration.


## Installation

    python setup.py install

In order to store a log file create a directory */var/log/dadump* with rights your user can right to it

## Configuration

Configuration file is placed at */etc/dadump/dadump.conf*

    [pg]
    db = postgresql://postgres@localhost:5432/postgres
    retention = 2
    destination = ~/dumps

In order to manage more database clusters add separate section:

    [mycluster]
    db = postgresql://postgres@localhost:5432/mydb
        postgresql://postgres@localhost:5432/mydb_00
        postgresql://postgres@localhost:5432/mydb_01
        postgresql://postgres@localhost:5432/mydb_02
        postgresql://postgres@localhost:5432/mydb_03
    retention = 4
    destination = ~/dumps/


## Commands

- **list** - show all dumps
- **drop** - delete a particular dump: drop name yyyy-mm-dd
- **run** - start dumping and cleanup old dumps
