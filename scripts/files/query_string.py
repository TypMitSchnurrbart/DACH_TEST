#!/usr/bin/python3
#!-*- coding: utf-8 -*-

import os
import sys
import urllib.parse
import bcrypt


def get_query_string():
    """
    Get Query String from environmental variables
    """

    #Default Case
    query_string = "Empty Data!"

    try:
        if os.environ['REQUEST_METHOD'] == "GET":
            query_string = os.environ['QUERY_STRING']

        else:
            query_string = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))

    #Differ except statement; this only for testing
    except KeyError:
        query_string = "vorname=Bonifaz&nachname=M%C3%BClp&strasse=Diitesberg&hausnummer=231&next_param=from_register_html"


    #Get parsed Version of query string
    query_string = parse_query_string(query_string)

    #Get the query_string seperated into data
    data_array = seperate_query_string(query_string)

    #Hashing of the Passwords
    data_array = hash_passwords(data_array)

    return data_array


def parse_query_string(query_string):
    """
    Resolving the UTF-8 HEX Codes to normal characters also "+" to spaces
    param:  query_string {string}
    return: query_string {string}
    """

    #Parsing out the Hex and the "+" into spacebars
    query_string = urllib.parse.unquote(query_string)
    query_string = urllib.parse.unquote_plus(query_string)
    
    return query_string


def seperate_query_string(query_string):
    """
    Seperate the Query String into the specific data elemts
    param:  query_string {string}
    return: data_array {list}
    """
    
    #Splitting into seperate Parameters
    data_array = query_string.split("&")

    #Splitting the list elements into id and value; Results in Arrays in an Array
    for i in range(0, len(data_array)):
        data_array[i] = data_array[i].split("=")

    return data_array


def hash_passwords(data_array):
    """
    Hashing potential passwords via bcrypt library
    """

    for i in range(0, len(data_array)):

        if data_array[i][0] == "password":
            salt = bcrypt.gensalt()
            data_array[i][1] = bcrypt.hashpw(data_array[0][1], salt)

        if data_array[i][0] == "password_repeat":
            salt = bcrypt.gensalt()
            data_array[i][1] = bcrypt.hashpw(data_array[0][1], salt)

    return data_array

def get_next_param(data_array):
    """
    Get the value of next_param to decide what to do
    """

    for i in range(0, len(data_array)):
        if data_array[i][0] == "next_param":

            next_param = data_array[i][1]

    return next_param
