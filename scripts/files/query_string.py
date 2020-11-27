#!/usr/bin/python3
#!-*- coding: utf-8 -*-

import os
import sys
import urllib.parse


def get_query_string():
    """
    Get Query String from environmental variables
    """

    #Default Case
    query_string = "Empty Data!"

    
    if os.environ['REQUEST_METHOD'] == "GET":
        query_string = os.environ['QUERY_STRING']

    else:
        query_string = sys.stdin.read(int(os.environ['CONTENT_LENGHT']))


    #Get parsed Version of query string
    query_string = parse_query_string(query_string)

    #Get the query_string seperated into data
    data_array = seperate_query_string(query_string)

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


def get_next_param():
    """
    Get the value of next_param to decide what to do
    """

    data_array = get_query_string()

    for i in range(0, len(data_array)):
        if data_array[i][0] == "next_param":

            next_param = data_array[i][1]

    return next_param
