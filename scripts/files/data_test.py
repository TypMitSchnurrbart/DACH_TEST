#!/usr/bin/python3
#!-*- coding: utf-8 -*-


import mariadb
import sys
import os

from test_file import test

try:
        conn = mariadb.connect(

            user="python",
            password="mdb17py8",
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


#TODO test
test()

