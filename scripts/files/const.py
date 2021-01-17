#!/usr/bin/python3
#!-*- coding: utf-8 -*-

#Version---------------------------------------------------------
VERSION = 1.0
LAST_UPDATE = "17.01.2021"

#Database Handle, Index 0: data_handle  Index 1: Connector-------
DATA_HANDLE = [None, None]

#Next_param values-----------------------------------------------
FROM_INDEX_HTML = "from_index_html"
FROM_REGISTER_HTML = "from_register_html"
FROM_MOVE = "from_move"
REPORT_INFECTION = "report_infection"
INFECTION_CONFIRMED = "infection_confirmed"

#App-Flag Value--------------------------------------------------
APP_FLAG = "app_flag"

#Error-Codes-----------------------------------------------------
GENERIC_ERROR = 1
REGISTER_INSERT_ERROR = 3
EMAIL_USED = 4
WRONG_PW_REPEAT = 5
EMAIL_NOT_KNOWN = 6
WRONG_LOGIN_PW = 7

#APP-Answers-----------------------------------------------------
APP_TRUE = "$true$"
APP_FALSE = "$false$" 

#Database-Column-NAMES-------------------------------------------
VORNAME = "vorname"
NACHNAME = "nachname"
COVID_STATE = "covid_state"
EMAIL = "email"
IDENT = "ident"

#Covid-State-Messages--------------------------------------------
NO_RISK_MESSAGE = "Kein Risiko"
LOW_RISK_MESSAGE = "Leichtes Risiko"
HIGH_RISK_MESSAGE = "Hohes Risiko"
INFECTED_MESSAGE = "Infiziert und Ansteckend"

#Covid-States----------------------------------------------------
NO_RISK = 0
LOW_RISK = 1
HIGH_RISK = 2
INFECTED = 3

#Relevant-Day-Limits---------------------------------------------
UPPER_LIMIT = 7
LOWER_LIMIT = 14