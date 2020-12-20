#!/usr/bin/python3
#!-*- coding: utf-8 -*-

def register_user(data_array, data_handle):
    """
    Inserts the user in the DACH Database
    param:  {list}  data_array; Containing the QueryString Information
    param:  {obj}   data_handle; Handle for MariaDB
    return: {bool}  True if a Error occurs, else False
    """

    #TODO Check if data_array contains valid data; especially password

    try:
        #TODO Change the TEST BOOL to 0 before rollout
        data_handle.execute(f"""INSERT INTO user (vorname, nachname, strasse, hausnr, plz, ort, email, password, TEST)
        VALUES ({data_array[0][1]}, {data_array[1][1]}, {data_array[2][1]}, {data_array[3][1]}, {data_array[4][1]}, {data_array[5][1]}, {data_array[6][1]}, {data_array[7][1]}, 1)""")

    except:
        return True

    return False


def verify_login(data_array, data_handle):
    """
    Verifys the Login of the User
    param:  {list}  data_array; Containing the QueryString Information
    param:  {obj}   data_handle; Handle for MariaDB
    return: {bool}  True if Error occurs, else False
    """

    return False