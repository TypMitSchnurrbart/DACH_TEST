#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.const import DATA_HANDLE

def get_error_text(error_code):
    """
    Get Error text from the dach_test DB via error_id
    param:  {int}  error_code
    return: {string} result
    """
    
    DATA_HANDLE[0].execute(f"SELECT output FROM error WHERE error_id = {error_code}")
    result = DATA_HANDLE[0].fetchall

    print(result)

    return result