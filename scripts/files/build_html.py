#!/usr/bin/python3
#!-*- coding: utf-8 -*-


#------------Default HTML Frame---Should be requiered everytime-----
def start_html(data_array):
	"""
	Make the requiered http and html header
	param:	{array} data_array; Input data from Post
	return:	{bool} To check if from APP or not
	"""

	for i in range(0, len(data_array)):
		if data_array[i][0] == "app_flag":
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

	int_style()

	return False


def int_style():
	"""
	Initialize style sheet
	"""
	print("""
	<style>
	</style>
	""")
	return


def test_body():

	print("""
	<h1>DHBW DACH Test Seite</h1>
	""")
	return


def end_html():
	print("\n</body>\n</html>")
	return