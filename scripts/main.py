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


#-----Main-----
if __name__ == "__main__":

	Error = False

	#Get MariaDB Handle
	data_handle = connect_mariadb()

	#Print HTML Credentials
	start_html()
	int_style()

	#Get DataArray and the NEXT Value
	data_array = get_query_string()
	next_param = get_next_param(data_array)

	#TODO Hash Password; both in register case!

	#SwitchCase for Next to differ Sites
	if next_param == "from_index_html":

		#Verify Login via Password and Email
		Error = verify_login(data_array, data_handle)

		if Error is False:
			show_homepage(data_array, data_handle)

	elif next_param == "from_register_html":

		#Register the new User
		Error = register_user(data_array, data_handle)

		if Error is False:
			show_homepage(data_array, data_handle)

	#Show a Test Body in Case next_param is empty
	else:
		test_body()


	if Error is True:
		#TODO Fehlerverarbeitung; index.html neu anzeigen? wie?
		print("Fehler aufgetreten!")


	#Close HTML
	end_html()

	