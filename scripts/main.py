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


#-----Main-----
if __name__ == "__main__":

	Error = False

	#Get MariaDB Handle
	data_handle = connect_mariadb()

	#Print HTTP/HTML Credentials
	start_html()

	#Get DataArray and the NEXT Value
	data_array = get_query_string()
	next_param = get_next_param(data_array)

	#SwitchCase for Next to differ Sites
	if next_param == "from_index_html":

		#Verify Login via Password and Email
		Error = verify_login(data_array, data_handle)

		if Error is False:
			show_homepage(data_array, data_handle)

		else:
			show_index_html()

	elif next_param == "from_register_html":

		#Register the new User
		Error = register_user(data_array, data_handle)

		if Error is False:
			show_homepage(data_array, data_handle)

		else:
			print(show_index_html())

	#Show a Test Body in Case next_param is empty
	else:
		Error = True


	#Close HTML
	end_html()
	data_handle.close()

	