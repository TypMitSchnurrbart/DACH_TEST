#!/usr/bin/python3
#!-*- coding: utf-8 -*-

#--Imports
import os
import sys

from files.query_string import get_next_param, get_query_string
from files.build_html import start_html

#-----Main-----
if __name__ == "__main__":

	start_html()

	print("Data Array: ", get_query_string())
	print("NEXT: ", get_next_param())
	