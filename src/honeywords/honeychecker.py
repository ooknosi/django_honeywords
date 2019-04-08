#!/usr/bin/env python3
"""Simple Honeychecker SQLite3 Server

Change settings below before use.

References
----------
`Honeywords Project <http://people.csail.mit.edu/rivest/honeywords/>`_

"""

from contextlib import closing
from os.path import isfile
from sqlite3 import connect
from sys import exit
from xmlrpc.server import SimpleXMLRPCServer

### Settings
IP = '192.168.56.101'
PORT = 55555
DATABASE = 'honeychecker_db.sqlite3'
###

def initialize():
    """Initializes Honeychecker database if it has not been created."""
    if not isfile(DATABASE):
        with closing(connect(DATABASE)) as conn:
            print(f"Creating database: {DATABASE}")
            print("Creating table:    indices")
            conn.execute("""CREATE TABLE indices (
                salt    TEXT    PRIMARY KEY     NOT NULL,
                idx     INT                     NOT NULL);"""
                )

def check_index(salt, index):
    """Checks validity of password index."""
    with closing(connect(DATABASE)) as conn:
        cur = conn.cursor()
        cur.execute('SELECT idx FROM indices WHERE salt=?;', (salt,))
        try:
            db_index = cur.fetchone()[0]
            is_valid = db_index == index
            print(f'Checking {salt}:{index} --> {is_valid}')
            return is_valid
        except IndexError:
            return False

def update_index(salt, index):
    """Inserts salt:index values into database."""
    with closing(connect(DATABASE)) as conn:
        cur = conn.cursor()
        print(f'Inserting new index: {salt}:{index}')
        try:
            cur.execute(
                'INSERT INTO indices (salt,idx) VALUES (?,?);', (salt, index,)
                )
            conn.commit()
        except Exception as e:
            print("Error: ", e)

def main():
    """Honeychecker server"""
    with SimpleXMLRPCServer((IP, PORT), allow_none=True) as honeychecker:
        initialize() 
        honeychecker.register_function(check_index, 'check_index')
        honeychecker.register_function(update_index, 'update_index')
        print(f"Honeychecker running at {IP}:{PORT} (Ctrl-C to stop)")
        try:
            honeychecker.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping Honeychecker")
            exit(0)

if __name__ == '__main__':
    main()
