#!/usr/bin/python3
#!-*- coding: utf-8 -*-

#--Imports
import os
import sys

from files.report import show_report_page, change_covid_state_infected
from files.query_string import get_next_param, get_query_string
from files.login import register_user, verify_login
from files.build_html import start_html, end_html
from files.index_html import show_index_html
from files.database import connect_mariadb
from files.home_page import show_homepage
from files.move import make_move

from files.const import DATA_HANDLE, FROM_INDEX_HTML, FROM_REGISTER_HTML, FROM_MOVE, GENERIC_ERROR, APP_FALSE, APP_TRUE
from files.const import REPORT_INFECTION, INFECTION_CONFIRMED


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
			print(APP_TRUE)

		#Respond to App as fail
		elif error is True and from_app is True:
			print(APP_FALSE)

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

	#To show Report Infection Site
	elif next_param == REPORT_INFECTION:
		show_report_page(data_array)

	#Showing Homepage after confirmend Infection
	#TODO Dara_array here will only contain the identifier! important for homepage!
	elif next_param == INFECTION_CONFIRMED:

		change_covid_state_infected(data_array)

		if from_app is True:
			print(APP_TRUE)
		else:
			show_homepage(data_array)

	#If next param is empty
	else:
		show_index_html(GENERIC_ERROR)


	#Close HTML / MariaDB
	if from_app is False:
		end_html()

	DATA_HANDLE[1].commit()
	DATA_HANDLE[1].close()

	