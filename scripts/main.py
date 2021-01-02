#!/usr/bin/python3
#!-*- coding: utf-8 -*-

#--Imports
import os
import sys

from files.query_string import get_next_param, get_query_string
from files.build_html import start_html, int_style, end_html, test_body
from files.database import connect_mariadb
from files.login import register_user, verify_login
from files.home_page import show_homepage
from files.index_html import show_index_html
from files.const import DATA_HANDLE
from files.move import make_move


#-----Main-----
if __name__ == "__main__":

	error = False
	error_code = None

	#Get MariaDB Handle
	connect_mariadb()

	#Print HTTP/HTML Credentials TODO Maybe only print if not from APP
	start_html()

	#Get data_array and the NEXT Value
	data_array = get_query_string()
	next_param = get_next_param(data_array)


	#Verify Login via Password and Email
	if next_param == "from_index_html":
		error, error_code = verify_login(data_array)

		if error is False:
			show_homepage(data_array)

		else:
			show_index_html(error_code)

	#Register the new User
	elif next_param == "from_register_html":
		error, error_code = register_user(data_array)

		if error is False:
			show_homepage(data_array)

		else:
			show_index_html(error_code)

	#Make the move
	elif next_param == "from_move":
		make_move(data_array)


	#If next param is empty
	else:
		show_index_html(error_code)

	#Close HTML / MariaDB
	end_html()
	DATA_HANDLE[1].commit()
	DATA_HANDLE[1].close()

	