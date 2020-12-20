#!/usr/bin/python3
#!-*- coding: utf-8 -*-


def show_homepage(data_array, data_handle):
    """
    Displaying the Body of the Home Page
    param:  {list}  data_array; Containing the QueryString Information
    param:  {obj}   data_handle; Handle for MariaDB
    """

    print("Welcome to the Homepage!")
    print(data_array)

    return