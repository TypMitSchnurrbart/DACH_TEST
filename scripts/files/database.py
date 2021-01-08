#!/usr/bin/python3
#!-*- coding: utf-8 -*-


import mariadb
import sys
import os

from files.const import DATA_HANDLE


def connect_mariadb():
    """
    Creating the Data Handle and Connector for MariaDB
    """
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
    

def get_user_data(data_array, string1, string2 = None, string3 = None):
    """
    Function to ask user data from the Database
    param:  {array} data_array; input data
    param:  {string} string1; requested column name
    param:  {string} string2; OPTIONAL
    param:  {string} string3; OPTIONAL
    return: {string/int/date} Requested Data in requested order
    """


    for i in range(0, len(data_array)):
        if data_array[i][0] == "email":
            given_email = data_array[i][1]
            break

        #TODO This will have to be changed; ident will be hash value of the email!
        elif data_array[i][0] == "ident":
            given_email = data_array[i][1]
            break

    if string2 is None and string3 is None:

        DATA_HANDLE[0].execute(f"SELECT {string1} FROM user WHERE user.email LIKE '{given_email}'")
        result = DATA_HANDLE[0].fetchall()
        return result[0][0]

    elif string3 is None:
        
        DATA_HANDLE[0].execute(f"SELECT {string1}, {string2} FROM user WHERE user.email LIKE '{given_email}'")
        result = DATA_HANDLE[0].fetchall()
        return result[0][0], result[0][1]

    else:
        
        DATA_HANDLE[0].execute(f"SELECT {string1}, {string2}, {string3} FROM user WHERE user.email LIKE '{given_email}'")
        result = DATA_HANDLE[0].fetchall()
        return result[0][0], result[0][1], result[0][2]