#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.get_data import get_user_data, get_user_id, get_last_room, get_visited_rooms, get_number_of_users
from files.const import VORNAME, NACHNAME, COVID_STATE, REPORT_INFECTION, LAST_UPDATE, VERSION, DATA_HANDLE
from files.error_handle import translate_covid_state
from files.query_string import get_query_string
from files.database import connect_mariadb

def start_http():
    """
    Creating the http header
    """

    print("Content-Type: application/json\n\n")

    return

def build_data_json(data_array):
    """
    Building the data json when requested
    param:  {list}  data_array; Containing the QueryString Information
    """

    #Getting the uid from current user
    activ_uid = get_user_id(data_array)

    #Like this only for test; Ident should be the email but somehow hashed
    ident_value = data_array[0][1]

    #Get the Covid_state from user
    covid_state = get_user_data(activ_uid, COVID_STATE)
    covid_state = translate_covid_state(covid_state)

    #Returns a String containing last room
    last_room = get_last_room(activ_uid)

    #Getting active user amount
    number_of_users = get_number_of_users()

    #Returns array like this: [(room, date, begin, end), (room, date, ....)] newest room with lowest index!
    last_rooms_array = get_visited_rooms(activ_uid)

    room_history = ""
    for i in range(0, len(last_rooms_array)):
        if i < len(last_rooms_array) - 1:
            room_history += f"""\t\t\t( "room": "{last_rooms_array[i][0]}", "date": "{last_rooms_array[i][1]}", "begin": "{last_rooms_array[i][2]}", "end": "{last_rooms_array[i][3]}"),\n"""
        elif i == len(last_rooms_array) - 1:
            room_history += f"""\t\t\t( "room": "{last_rooms_array[i][0]}", "date": "{last_rooms_array[i][1]}", "begin": "{last_rooms_array[i][2]}", "end": "{last_rooms_array[i][3]}")"""

    output = f"""(
    "ident_value": "{ident_value}",
    "state": "{covid_state}",
    "lastRoom": "{last_room}",
    "activeUser": "{number_of_users}",            
    "lastUpdate": "{LAST_UPDATE}",
    "version": "{VERSION}",
    "roomHistory":  [
{room_history}
                    ]
)"""
    output = output.replace("(", "{")
    output = output.replace(")", "}")

    print(output)

    return

if __name__ == "__main__":

    #HTTP-Header
    start_http()

    #Getting DB Connection
    connect_mariadb()

    #Parse Query String
    #data_array = get_query_string()
    data_array = [["ident", "alexm01@freenet.de"], ["next_param", "from_testing"]]

    #Build JSON
    build_data_json(data_array)

    #Closing DB Connection
    DATA_HANDLE[1].commit()
    DATA_HANDLE[1].close()
