#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.database import get_user_data
from files.const import VORNAME, NACHNAME, COVID_STATE, REPORT_INFECTION
from files.error_handle import translate_covid_state

def show_homepage(data_array):
    """
    Displaying the Body of the Home Page
    param:  {list}  data_array; Containing the QueryString Information
    """

    vorname, nachname, covid_state = get_user_data(data_array, VORNAME, NACHNAME, COVID_STATE)
    covid_state = translate_covid_state(covid_state)

    #Like this only for test; Ident should be the email but somehow hashed
    ident_value = data_array[0][1]

output = f"""{
    "ident_value": "{ident_value}",
    "status": "{covid_state}",
    "room": [
        "room1": "{room1}",
        "room2": "{room2}",
        "room3": "{room3}",
        "room4": "{room4}",
    ],
    "date": "{date}"
}
"""

print(output)

#TODO Delete MOVE_Test from sidenav
#TODO Hash the ident; store in extra db table; not to pretty but should be alright
return