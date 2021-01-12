#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.const import DATA_HANDLE, NO_RISK_MESSAGE, LOW_RISK_MESSAGE, HIGH_RISK_MESSAGE, INFECTED_MESSAGE

def get_error_text(error_code):
    """
    Get Error text from the dach_test DB via error_id
    param:  {int}  error_code
    return: {string} result
    """

    DATA_HANDLE[0].execute(f"SELECT error, output FROM error WHERE error_id = '{error_code}'")
    result = DATA_HANDLE[0].fetchall()

    return result


def translate_covid_state(covid_state):
    """
    Translating the stored ID for Covid-State to actual Messages from const
    """
    
    if covid_state == 0:
        return NO_RISK_MESSAGE

    elif covid_state == 1:
        return LOW_RISK_MESSAGE

    elif covid_state == 2:
        return HIGH_RISK_MESSAGE

    elif covid_state == 3:
        return INFECTED_MESSAGE
        