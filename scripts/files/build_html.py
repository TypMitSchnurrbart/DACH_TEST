#!/usr/bin/python3
#!-*- coding: utf-8 -*-


#------------Default HTML Frame---Should be requiered everytime-----
def start_html(data_array):
	"""
	Make the requiered http and html header
	"""

	for i in range(0, len(data_array)):
		if data_array[i][0] == "app_flag":
			print("Content-Type: text/html")
			print("")
			return

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


def test_body():

	print("""
	<h1>DHBW DACH Test Seite</h1>
	""")
	return


def end_html():

	print("\n</body>\n</html>")
	return