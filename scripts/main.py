#!/usr/bin/python3
#!-*- coding: utf-8 -*-

#--Imports
import os
import sys

from files.query_string import get_next_param, get_query_string
from files.build_html import start_html, end_html
from files.database import connect_mariadb
from files.login import register_user, verify_login
from files.home_page import show_homepage
from files.index_html import show_index_html
from files.move import make_move

from files.const import DATA_HANDLE, FROM_INDEX_HTML, FROM_REGISTER_HTML, FROM_MOVE, GENERIC_ERROR, APP_LOGIN_FALSE, APP_LOGIN_TRUE



#-----Main-----
if __name__ == "__main__":

	error = False
	from_app = False
	error_code = None

	#Get MariaDB Handle
	connect_mariadb()

	#Get data_array and the NEXT Value
	data_array = get_query_string()
	next_param = get_next_param(data_array)

	#Print HTTP/HTML Credentials
	from_app = start_html(data_array)


	#Verify Login via Password and Email
	if next_param == FROM_INDEX_HTML:

		error, error_code = verify_login(data_array)


		#Display Homepage as logged in
		if error is False and from_app is False:
			show_homepage(data_array)

		#Respond to App as success TODO own functions!
		elif error is False and from_app is True:
			print(APP_LOGIN_TRUE)

		#Respond to App as fail
		elif error is True and from_app is True:
			print(APP_LOGIN_FALSE)

		else:
			show_index_html(error_code)


	#Register the new User
	elif next_param == FROM_REGISTER_HTML:
		error, error_code = register_user(data_array)

		if error is False:
			show_homepage(data_array)
		else:
			show_index_html(error_code)


	#Make the move
	elif next_param == FROM_MOVE:
		make_move(data_array)


	#If next param is empty
	else:
		show_index_html(GENERIC_ERROR)


	#Close HTML / MariaDB
	if from_app is False:
		end_html()

	DATA_HANDLE[1].commit()
	DATA_HANDLE[1].close()

	