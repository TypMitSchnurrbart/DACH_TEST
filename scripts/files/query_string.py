#!/usr/bin/python3
#!-*- coding: utf-8 -*-

import os
import sys
import urllib.parse
import hashlib


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

    #Hashing of the Passwords, but only in the register case , else hash later
    for i in range(len(data_array)):
        if data_array[i][1] == "from_register_html":
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
    Hashing potential passwords via hashlib, take in data_array,
    return the data_array with hashed passwords
"""
    # Salt needs to be initialized before cause the passwords should evaluate to the same hash

    salt = os.urandom(32)       # returns 32 random Bytes

    # search for the password in the data, also the list has to be modified to hold the hash and the salt

    for i in range(len(data_array)):
        if data_array[i][0] == "password":
            data_array[i][1] = compute_hash(data_array[i][1], salt)
            data_array[i][2] = salt        # maybe this should be a seperate entry called salt

        elif data_array[i][0] == "password_repeat":
            data_array[i][1] = compute_hash(data_array[i][1], salt)
            data_array[i][2] = salt        # maybe this should be a seperate entry called salt

    return data_array


def compute_hash(password, salt):
    key = hashlib.pbkdf2_hmac(      # will be a 64 Byte sequence
        'sha256',
        password.encode('utf-8'),
        salt,
        100000  # Amount of iterations for the hashing alorithm, at least 100000 is recommended
    )
    return key.hex()    # this is a string for whatever reason, but perfect for this application, just 64 chars


def get_next_param(data_array):
    """
    Get the value of next_param to decide what to do
    param:  {array} data_array; list with all the data
    """

    next_param = ""

    for i in range(0, len(data_array)):
        if data_array[i][0] == "next_param":

            next_param = data_array[i][1]

    return next_param
