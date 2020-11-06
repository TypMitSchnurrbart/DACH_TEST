#!/usr/bin/python3
#!-*- coding: utf-8 -*-

import os


def get_query_string():
	"""
	Get query string from environment variables of the os
	"""
	return os.environ.get("QUERY_STRING", "Empty Query String in URL!")


def make_html_header():
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

	<style>
		body {
			width: 35em;
			margin: 0 auto;
			font-family: Tahoma, Verdana, Arial, sans-serif;
		}
	</style>
	""")
	return

def start_html_body():

	print("""
	<body>
	<h1>DHBW DACH Test Seite</h1>
	""")
	return

def query_string_test(query_string):

	print("""
	<h1>This is the given Input as Query String: {0}</h1>""" .format(query_string))
	return


def end_html():

	print("\n</body>\n</html>")
	return


if __name__ == "__main__":

	make_html_header()
	start_html_body()
	query_string_test(get_query_string())
	end_html()

