#!/usr/bin/python3
#!-*- coding: utf-8 -*-

#--Imports
import os
import sys

#------------Default HTML Frame---Should be requiered everytime-----
def start_html():
	"""
	Make the requiered http and html header
	"""

	print("Content-Type: text/html")
	print("")
	print("""
	<html>
		<head>
			<title>DACH DHBW</title>
			<meta http-equiv="content-type" content="text/html; charset=utf-8">

		</head>
	""")
	return


def int_style():
	"""
	Initialize style sheet
	"""
	print("""
	<style>

	</style>
	""")
	return


def start_body():

	print("""
	<body>
	<h1>DHBW DACH Test Seite</h1>
	""")
	return


def end_html():

	print("\n</body>\n</html>")
	return


#------QueryString Test can be removed or edited------
def get_query_string():
	"""
	Get query string from environment variables of the os
	"""

	query_string = "Empty Data!"

	if os.environ['REQUEST_METHOD'] == "GET":
		query_string = os.environ['QUERY_STRING']

	else:
		query_string = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))

	return query_string

def query_string_test(query_string):

	print("""
	<h2>This is the given Input as Query String: {0}</h2>""" .format(query_string))
	return


#-----Main-----
if __name__ == "__main__":

	start_html()
	int_style()
	start_body()
	query_string_test(get_query_string())
	end_html()

