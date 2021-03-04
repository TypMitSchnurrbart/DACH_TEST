#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.const import DATA_HANDLE

#-----------------------------------------------------------------------------------------------------------------------------------
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


#-----------------------------------------------------------------------------------------------------------------------------------
def get_user_id(data_array):
    """
    Getting the uid to email/ident from data_array
    param:  {array} data_array; input from http
    return:  {int}   uid;        user id in DB
    """ 

    for i in range(0, len(data_array)):
        if data_array[i][0] == "email":
            given_email = data_array[i][1]
            break

        elif data_array[i][0] == "ident":
            #TODO This will have to be changed; ident will be hash value of the email! Different Case if ident is our hash value!!
            given_email = data_array[i][1]
            break

            
    DATA_HANDLE[0].execute(f"SELECT uid FROM user WHERE user.email LIKE '{given_email}'")
    result = DATA_HANDLE[0].fetchall()
    return result[0][0]


#-----------------------------------------------------------------------------------------------------------------------------------
def get_last_room(activ_uid, from_json = False):
    """
    Getting the Last visited Room of a Person
    param:  {int}       activ_uid   user_id of current user
    return:  {string}    last_room   last visited room of user
    """

    #TODO try/except with error codes!

    #Getting last visited room_id
    DATA_HANDLE[0].execute(f"SELECT room FROM movement WHERE person = {activ_uid} ORDER BY move_id DESC LIMIT 1;")
    result = DATA_HANDLE[0].fetchall()
    
    #Translate room_id to room description as string, can be empty set
    if result != []:
        DATA_HANDLE[0].execute(f"SELECT description FROM room WHERE room_id = {result[0][0]}")
        result = DATA_HANDLE[0].fetchall()

        return result[0][0]

    else:
        if from_json is False:
            return " - "
        else:
            return "$false$"


#-----------------------------------------------------------------------------------------------------------------------------------
def get_visited_rooms(activ_uid, from_json = False):
    """
    Get the five last visited rooms with date and times
    param:  {int}   activ_uid       uid from activ user
    return: {array} visited_rooms   array with all visited rooms, can have index in range 0, 4! According output
    """

    #TODO try/excepts

    #Get last visited rooms; max. amount = 5
    DATA_HANDLE[0].execute(f"""SELECT description, DATE_FORMAT(date, '%d.%m.%Y'), TIME_FORMAT(begin, '%H:%i'), TIME_FORMAT(end, '%H:%i') FROM movement JOIN room ON movement.room = room.room_id 
    WHERE person = {activ_uid} AND end IS NOT NULL ORDER BY move_id DESC LIMIT 5""")
    result = DATA_HANDLE[0].fetchall()

    if result != []:
        return result
    elif from_json is True and result == []:
        mock_array = [["$false$", "$false$", "$false$", "$false$"]]
        return mock_array 
    
    elif from_json is False and result == []:
        mock_array = [[" - ", " - ", " - ", " - "]]
        return mock_array

#-----------------------------------------------------------------------------------------------------------------------------------
def get_number_of_users():
    """
    Get the number of registered users from DACH
    return: {int}   Number of registered users
    """

    DATA_HANDLE[0].execute(f"SELECT count(uid) FROM user")
    result = DATA_HANDLE[0].fetchall()

    return result[0][0]