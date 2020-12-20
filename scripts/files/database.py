#!/usr/bin/python3
#!-*- coding: utf-8 -*-


import mariadb
import sys
import os


def connect_mariadb():
    try:
            connect = mariadb.connect(

                user="python",
                password="mdb17py8",
                host="localhost",
                port=3306,
                database="dach_test"
            )
    except mariadb.Error as error_message:
        print(f"Error connecting to MariaBD Platform: {error_message}")
        sys.exit(321)

    maria_connector = connect.cursor()

    return maria_connector
    
