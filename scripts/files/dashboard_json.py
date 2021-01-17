#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.get_data import get_user_data
from files.const import VORNAME, NACHNAME, COVID_STATE, REPORT_INFECTION
from files.error_handle import translate_covid_state

def build_data_json(data_array):
    """
    Building the data json when requested
    param:  {list}  data_array; Containing the QueryString Information
    """

    vorname, nachname, covid_state = get_user_data(data_array, VORNAME, NACHNAME, COVID_STATE)
    covid_state = translate_covid_state(covid_state)

    #Like this only for test; Ident should be the email but somehow hashed
    ident_value = data_array[0][1]

    #TODO make a full own module for the json request to update the dashboard!!! <------------------


    roomInfo = transmitData
    for i in roomInfo:
        pass
                # ( "room": "{room1}", "date": "{date1}", "time": "{time1}", "nrUser": "{nrUser1}"),
                # ( "room": "{room2}", "date": "{date2}", "time": "{time2}", "nrUser": "{nrUser2}"),
                # ( "room": "{room3}", "date": "{date3}", "time": "{time3}", "nrUser": "{nrUser3}"),
                # ( "room": "{room4}", "date": "{date4}", "time": "{time4}", "nrUser": "{nrUser4}"),
                # ( "room": "{room5}", "date": "{date5}", "time": "{time5}", "nrUser": "{nrUser5}")


    output = f"""
        (
            "ident_value": "{ident_value}",
            "state": "{state}",
            "lastRoom": "{lastRoom}",
            "activeUser": "{activeUser}",
            "lastUpdate": "{lastUpdate}",
            "version": "{version}",
            "roomHistory": [
                {roomHistory}
            ]
        )
    """
    output = output.replace("(", "{")
    output = output.replace(")", "}")

    print(output)

    #TODO Delete MOVE_Test from sidenav
    #TODO Hash the ident; store in extra db table; not to pretty but should be alright
    return