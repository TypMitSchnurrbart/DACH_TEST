#!/usr/bin/python3
#!-*- coding: utf-8 -*-


#Database Handle, Index 0: data_handle  Index 1: Connector-------
DATA_HANDLE = [None, None]

#Next_param values-----------------------------------------------
FROM_INDEX_HTML = "from_index_html"
FROM_REGISTER_HTML = "from_register_html"
FROM_MOVE = "from_move"

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
APP_LOGIN_TRUE = "$true$"
APP_LOGIN_FALSE = "$false$"

#Database-Column-NAMES-------------------------------------------
VORNAME = "vorname"
NACHNAME = "nachname"
COVID_STATE = "covid_state"

#Covid-State-Messages--------------------------------------------
NO_RISK_MESSAGE = "Kein Risiko"
LOW_RISK_MESSAGE = "Leichtes Risiko"
HIGH_RISK_MESSAGE = "Hohes Risiko"
INFECTED_MESSAGE = "Infiziert und Ansteckend"