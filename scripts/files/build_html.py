#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.const import APP_FLAG

#------------Default HTML Frame---Should be requiered everytime-----
def start_html(data_array):
	"""
	Make the requiered http and html header
	param:	{array} data_array; Input data from Post
	return:	{bool} To check if from APP or not
	"""

	for i in range(0, len(data_array)):
		if data_array[i][0] == APP_FLAG:
			print("Content-Type: text/html")
			print("")
			return True

	print("Content-Type: text/html")
	print("")
	print("""<html>
	<head>
		<title>DACH DHBW</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8">

	</head>
	<body>
	""")

	return False


def end_html():
	print("\n</body>\n</html>")
	return