#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.const import DATA_HANDLE

def get_user_data(activ_uid, string1, string2 = None, string3 = None):
    """
    Function to ask user data from the Database easily
    param:  {int} activ_uid; input data
    param:  {string} string1; requested column name
    param:  {string} string2; OPTIONAL
    param:  {string} string3; OPTIONAL
    return: {string/int/date} Requested Data in requested order
    """

    #TODO Use this Code for the get user info for App

    if string2 is None and string3 is None:

        DATA_HANDLE[0].execute(f"SELECT {string1} FROM user WHERE user.uid = {activ_uid}")
        result = DATA_HANDLE[0].fetchall()
        return result[0][0]

    elif string3 is None:
        
        DATA_HANDLE[0].execute(f"SELECT {string1}, {string2} FROM user WHERE user.uid = {activ_uid}")
        result = DATA_HANDLE[0].fetchall()
        return result[0][0], result[0][1]

    else:
        
        DATA_HANDLE[0].execute(f"SELECT {string1}, {string2}, {string3} FROM user WHERE user.uid = {activ_uid}")
        result = DATA_HANDLE[0].fetchall()
        return result[0][0], result[0][1], result[0][2]


def get_user_id(data_array):
    """
    Getting the uid to email/ident from data_array
    param:  {array} data_array; input from http
    return:  {int}   uid;        user id in DB
    """

    #TODO This will have to be changed; ident will be hash value of the email! Different Case if ident is our hash value!! 

    for i in range(0, len(data_array)):
        if data_array[i][0] == "email":
            given_email = data_array[i][1]
            break

        elif data_array[i][0] == "ident":
            given_email = data_array[i][1]
            break

            
    DATA_HANDLE[0].execute(f"SELECT uid FROM user WHERE user.email LIKE '{given_email}'")
    result = DATA_HANDLE[0].fetchall()
    return result[0][0]


def get_last_room(activ_uid):
    """
    Getting the Last visited Room of a Person
    param:  {int}       activ_uid   user_id of current user
    return:  {string}    last_room   last visited room of user
    """

    #TODO try/except with error codes!

    DATA_HANDLE[0].execute(f"SELECT room FROM movement WHERE person = {activ_uid} ORDER BY move_id DESC LIMIT 1;")
    result = DATA_HANDLE[0].fetchall()
    
    DATA_HANDLE[0].execute(f"SELECT description FROM room WHERE room_id = {result[0][0]}")
    result = DATA_HANDLE[0].fetchall()

    return result[0][0]

def get_visited_rooms(activ_uid):
    """
    Get the five last visited rooms with date and times
    param:  {int}   activ_uid       uid from activ user
    return: {array} visited_rooms   array with all visited room, can have index in range 0, 4! According output
    """

    raise NotImplementedError