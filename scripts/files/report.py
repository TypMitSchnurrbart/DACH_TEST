#!/usr/bin/python3
#! -*- coding: utf-8 -*-

from files.const import INFECTION_CONFIRMED, DATA_HANDLE, LOW_RISK, HIGH_RISK, INFECTED, UPPER_LIMIT, LOWER_LIMIT, EMAIL, IDENT

def show_report_page(data_array):

    #TODO This is like this just for testing!
    for i in range(0 , len(data_array)):
        if data_array[i][0] == IDENT:
            ident_value = data_array[i][1]
            break
        elif data_array[i][0] == EMAIL:
            ident_value = data_array[i][1]
            break

    output = f"""<!DOCTYPE html>
<html lang="de">
    <head>
        <title>DACH DHBW - Registrierung</title>
        <meta charset="UTF-8">
        <meta name="author" charset="Dirk Hattemer, Alexander Müller">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://kit.fontawesome.com/672bee8847.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="/style.css">
    </head>
    <body>
        <nav id="topNav" class="overlay-nav">
            <div class="overlay-nav-content">
                <a href="javascript:void(0)" class="closebtn" id="closeNav">&times;</a>
                <a class="active" href="/index.html">Home</a>
                <a href="/HTML/dashboard.html">Dashboard</a>
                <a href="/HTML/login.html">Login</a>
                <a href="/HTML/register.html">Registrierung</a>
            </div>
        </nav>
        <div class="main-content">
            <header>
                <div class="main-header">
                    <div class="nav-icon">
                        <span id="openNav">&#9776;</span>
                    </div>
                    <div class="dach-logo">
                        <div></div>
                    </div>
                </div>
            </header>
            <main>
                <section class="main">
                    <div>
                        <h1>Krankmeldung</h1>
                    </div>
                    <div>
                        <h3>Bestätigen Sie hier dass sie Infiziert sind:<h3>
                        <form method="post" action="/scripts/main.py">
                            <input type="hidden" id="ident" name="ident" value={ident_value}>
                            <input type="hidden" id="next_param" name="next_param" value={INFECTION_CONFIRMED}>
                            <button type="submit">Ja. Ich bin infiziert</button>
                        </form>
                    </div>
                </section>
            </main>
            <footer>
                <nav>
                    <div>
                        <ul class="footer-nav">
                            <li>&copy;DACH</li>
                            <li><a href="/HTML/impressum.html">Impressum</a></li>
                            <li><a href="/HTML/erklaerung.html">Datenschutzerklärung</a></li>
                        </ul>
                    </div>
                </nav>
            </footer>
        </div>
        <script src="/JavaScript/index.js"></script>
        <script src="/JavaScript/registerValidation.js"></script>
    </body>
</html>
"""

    print(output)

    #TODO Hash the ident; store in extra db table; not to pretty but should be alright

    return


def change_covid_state_infected(data_array):
    """
    Change all the Corona States after a reported Infection.
    param: {array} data_array; Input Data, here only ident interesting
    """
    #Data_array should look like this have email on index [0][1]


    #TODO ident still holds the email, future it should hold a hash value that is linked to a user in a different table
    #TODO therefore must this query be changed in the future!

    #TODO trys/ecxepts with own error codes and Messages!

    DATA_HANDLE[0].execute(f"""UPDATE user SET covid_state = {INFECTED}, covid_set_date = CURDATE() WHERE email LIKE '{data_array[0][1]}'""")


    #Set all contacted people to risk states----------------------------------------------------

    high_risk_ids = []
    low_risk_ids = []

    #Get uid from infected
    DATA_HANDLE[0].execute(f"""SELECT uid FROM user WHERE email LIKE '{data_array[0][1]}'""")
    result = DATA_HANDLE[0].fetchall()
    infected_id = result[0][0]

    #Get all visited rooms/date/begin/end from infected
    DATA_HANDLE[0].execute(f"""SELECT room, date, begin, end from movement WHERE person = {infected_id}""")
    result = DATA_HANDLE[0].fetchall()

    #Set the risk ids
    for i in range(0, len(result)):
        infected_begin = result[i][2]
        infected_end = result[i][3]

        #Get low risk persons and save them
        DATA_HANDLE[0].execute(f"""SELECT person FROM movement WHERE person != {infected_id} AND room = {result[i][0]} AND date = '{result[i][1]}' AND 
        covid_state <= 1 AND (date >= CURDATE() - INTERVAL {LOWER_LIMIT} DAY) AND (date < CURDATE() - INTERVAL {UPPER_LIMIT} DAY) AND
        ((begin <= '{infected_begin}' AND end <= '{infected_end}' AND end >= '{infected_begin}') OR (begin >= '{infected_begin}' AND end >= '{infected_end}' AND begin <= '{infected_end}') OR
        (begin >= '{infected_begin}' AND end <= '{infected_end}') OR (begin <= '{infected_begin}' AND end >= '{infected_end}'))""")

        low_risk_person = DATA_HANDLE[0].fetchall()
        for i in range(0, len(low_risk_person)):
            low_risk_ids.append(low_risk_person[i][0])

        #Get high risk persons and save them
        DATA_HANDLE[0].execute(f"""SELECT person FROM movement WHERE person != {infected_id} AND room = {result[i][0]} AND date = '{result[i][1]}' AND 
        covid_state <= 2 AND (date >= CURDATE() - INTERVAL {UPPER_LIMIT} DAY) AND
        ((begin <= '{infected_begin}' AND end <= '{infected_end}' AND end >= '{infected_begin}') OR (begin >= '{infected_begin}' AND end >= '{infected_end}' AND begin <= '{infected_end}') OR
        (begin >= '{infected_begin}' AND end <= '{infected_end}') OR (begin <= '{infected_begin}' AND end >= '{infected_end}'))""")

        high_risk_person = DATA_HANDLE[0].fetchall()
        for i in range(0, len(high_risk_person)):
            high_risk_ids.append(high_risk_person[i][0])
        

    #Set the accroding covid_states
    for i in range(0, len(low_risk_ids)):
        DATA_HANDLE[0].execute(f"""UPDATE user SET covid_state = {LOW_RISK}, covid_set_date = CURDATE() WHERE uid = {low_risk_ids[i]}""")

    for i in range(0, len(high_risk_ids)):
        DATA_HANDLE[0].execute(f"""UPDATE user SET covid_state = {HIGH_RISK}, covid_set_date = CURDATE() WHERE uid = {high_risk_ids[i]}""")

    return