#!/usr/bin/python3
#!-*- coding: utf-8 -*-
from files.query_string import compute_hash
from files.const import DATA_HANDLE

def register_user(data_array):
    """
    Inserts the user in the DACH Database
    param:  {list}  data_array; Containing the QueryString Information
    return: {bool}  True if a Error occurs, else False
    return: {int}   ErrorID form Database
    """

    #Password and Password Repeat must be the same
    if data_array[7][1] != data_array[8][1]:
        return True, 5


    #Check for unique email in Database
    DATA_HANDLE[0].execute(f"SELECT uid FROM user WHERE user.email LIKE '{data_array[6][1]}'")
    result = DATA_HANDLE[0].fetchall()

    if result != []:
        return True, 4

    #Try SQL Insert
    try:
        #Always be aware of strings in SQL Statements
        DATA_HANDLE[0].execute(f"""INSERT INTO user (vorname, nachname, strasse, hausnr, plz, ort, email, password, salt) VALUES ("{data_array[0][1]}", "{data_array[1][1]}", "{data_array[2][1]}", {data_array[3][1]}, {data_array[4][1]}, "{data_array[5][1]}", "{data_array[6][1]}", "{data_array[7][1]}" , "{data_array[7][2]}")""")

    except:
        return True, 3

    return False, None


def verify_login(data_array):
    """
    Verifys the Login of the User
    param:  {list}  data_array; Containing the QueryString Information
    return: {bool}  True if Error occurs, else False
    """

    error = False
    error_code = None
    from_app = False

    given_email = data_array[0][1]
    given_password = data_array[1][1]

    DATA_HANDLE[0].execute(f"SELECT uid, password, salt FROM user WHERE user.email LIKE '{given_email}'")

    #Result will Look like: [(uid, "password", "salt")]; so a Tupel in a List
    result = DATA_HANDLE[0].fetchall()

    #Check if Result is Empty(Email not know) and if password is the same
    if result == []:
        error = True
        error_code = 6

    if result[0][1] != compute_hash(given_password, result[0][2]):
        error = True
        error_code = 7

    #TODO Here we could set a global variable as active user with now known uid!

    #Check if from app or not
    for i in range(0, len(data_array)):
        if data_array[i][0] == "app_flag":
            from_app = True

    return error, error_code, from_app