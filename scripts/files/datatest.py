#!/usr/bin/python3
#!-*- coding: utf-8 -*-


import mariadb
import sys
import os

try:
        conn = mariadb.connect(

            user="python",
            password=f"{os.environ['PYTHON_MARIADB_PW']}",
            host="localhost",
            port=3306,
            database="dach_test"
        )
except mariadb.Error as error_message:
    print(f"Error connecting to MariaBD Platform: {error_message}")
    sys.exit(321)



print("Content-Type: text/html\n\n")


#-----Funktion von Mariadb Handler
cur = conn.cursor()


cur.execute("SELECT vorname, nachname FROM user")

for (vorname, nachname) in cur:
    print(f"{vorname} {nachname} - kranker Typ <br/>")

