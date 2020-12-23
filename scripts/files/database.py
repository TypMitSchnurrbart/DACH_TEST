#!/usr/bin/python3
#!-*- coding: utf-8 -*-


import mariadb
import sys
import os

from files.const import DATA_HANDLE


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

    DATA_HANDLE[0] = maria_connector
    DATA_HANDLE[1] = connect

    return maria_connector, connect
    
