#!/usr/bin/python3
#!-*- coding: utf-8 -*-

def register_user(data_array, data_handle):
    """
    Inserts the user in the DACH Database
    param:  {list}  data_array; Containing the QueryString Information
    param:  {obj}   data_handle; Handle for MariaDB
    return: {bool}  True if a Error occurs, else False
    """

    #TODO Check if data_array contains valid data; especially password = repeat_pw and unique email! Otherwise Return True!

    try:
        #Always be aware of strings in SQL Statements
        data_handle.execute(f"""INSERT INTO user (vorname, nachname, strasse, hausnr, plz, ort, email, password) VALUES ("{data_array[0][1]}", "{data_array[1][1]}", "{data_array[2][1]}", {data_array[3][1]}, {data_array[4][1]}, "{data_array[5][1]}", "{data_array[6][1]}", "{data_array[7][1]}")""")

    except:
        print("Error in SQL Insertion!")
        return True

    return False


def verify_login(data_array, data_handle):
    """
    Verifys the Login of the User
    param:  {list}  data_array; Containing the QueryString Information
    param:  {obj}   data_handle; Handle for MariaDB
    return: {bool}  True if Error occurs, else False
    """

    given_email = data_array[0][1]
    given_password = data_array[1][1]

    data_handle.execute(f"SELECT uid, password FROM user WHERE user.email LIKE '{given_email}'")

    #Result will Look like: [(uid, "password")]; so a Tupel in a List
    result = data_handle.fetchall()

    #Check if Result is Empty(Email not know) and if password is the same
    if result == []:
        return True

    if result[0][1] != given_password:
        return True

    #TODO Here we could set a global variable as active user with now known uid!

    return False