#!/usr/bin/python3
#!-*- coding: utf-8 -*-

import os
import hashlib

def hash_passwords(data_array):
    """
    Hashing potential passwords via hashlib, take in data_array,
    return the data_array with hashed passwords
    param:  {array} data_array; The input data
    return: {array} data_array; With now hashed pw and the salt value
    """

    #Salt needs to be initialized before cause the passwords should evaluate to the same hash
    #Returns 32 random Bytes
    salt = os.urandom(32)

    #Search for the password in the data, also the list has to be modified to hold the hash and the salt
    for i in range(len(data_array)):
        if data_array[i][0] == "password":
            data_array[i][1] = compute_hash(data_array[i][1], salt)
            data_array[i].append(salt)          #Maybe this should be a seperate entry called salt

        elif data_array[i][0] == "password_repeat":
            data_array[i][1] = compute_hash(data_array[i][1], salt)
            data_array[i].append(salt)          #Maybe this should be a seperate entry called salt

    return data_array


def compute_hash(password, salt):
    """
    Compute the Hash Value with sha256
    param:  {string} password; given pw from data_array
    param:  salt; init salt value
    return: {string} key.hex()
    """
    key = hashlib.pbkdf2_hmac(                  #Will be a 64 Byte sequence
        'sha256',
        password.encode('utf-8'),
        salt,
        100000                                  #Amount of iterations for the hashing alorithm, at least 100000 is recommended
    )
    return key.hex()                            #This is a string for whatever reason, but perfect for this application, just 64 chars
