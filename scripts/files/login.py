#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.hashing import compute_hash
from files.const import DATA_HANDLE, WRONG_PW_REPEAT, EMAIL_USED, REGISTER_INSERT_ERROR, EMAIL_NOT_KNOWN, WRONG_LOGIN_PW

import base64

def register_user(data_array):
    """
    Inserts the user in the DACH Database
    param:  {list}  data_array; Containing the QueryString Information
    return: {bool}  True if a Error occurs, else False
    return: {int}   ErrorID form Database
    """

    #Password and Password Repeat must be the same
    if data_array[7][1] != data_array[8][1]:
        return True, WRONG_PW_REPEAT


    #Check for unique email in Database
    DATA_HANDLE[0].execute(f"SELECT uid FROM user WHERE user.email LIKE '{data_array[6][1]}'")
    result = DATA_HANDLE[0].fetchall()

    if result != []:
        return True, EMAIL_USED


    #Try SQL Insert
    try:
        #Always be aware of strings in SQL Statements
        #weird syntax for saving the salt ensures only the base64-string is saved and easily selectable
        DATA_HANDLE[0].execute(f"""INSERT INTO user (vorname, nachname, strasse, hausnr, plz, ort, email, password, salt) VALUES ("{data_array[0][1]}", "{data_array[1][1]}", "{data_array[2][1]}", {data_array[3][1]}, {data_array[4][1]}, "{data_array[5][1]}", "{data_array[6][1]}", "{data_array[7][1]}" , "{str(base64.b64encode(data_array[7][2]))[2:-1]}")""")
        
    except:
        return True, REGISTER_INSERT_ERROR

    return False, None


def verify_login(data_array):
    """
    Verifys the Login of the User
    param:  {list}  data_array; Containing the QueryString Information
    return: {bool}  True if Error occurs, else False
    """

    #TODO Delete Print
    #print(f"\nInput Daten: {data_array}")

    given_email = data_array[0][1]
    given_password = data_array[1][1]

    DATA_HANDLE[0].execute(f"SELECT uid, password, salt FROM user WHERE user.email LIKE '{given_email}'")

    #Result will Look like: [(uid, "password", "salt")]; so a Tupel in a List
    result = DATA_HANDLE[0].fetchall()

    #TODO Delete Print
    #print(f"\ngiven_email: {given_email}\ngiven_password: {given_password}\n result: {result}")

    #Check if Result is Empty(Email not know) and if password is the same
    if result == []:
        return True, EMAIL_NOT_KNOWN
      
    if result[0][1] != compute_hash(given_password, base64.b64decode(result[0][2])):
        return True, WRONG_LOGIN_PW

    #TODO User should stay logged in -> hidden value in every form therefore set global var with uid that is in all possible forms that get generated

    return False, None