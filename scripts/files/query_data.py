#!/usr/bin/python3
#!-*- coding: utf-8 -*-

import sys
import os


def get_query_string():
	"""
	Get query string from environment variables of the os
	"""

	query_string = "Empty Data!"

    
	if os.environ['REQUEST_METHOD'] == "GET":
		query_string = os.environ['QUERY_STRING']

	else:
		query_string = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
    
    query_string = "email=alexm01%40freenet.de&password=sd&next_param=from_index_html"

    return query_string