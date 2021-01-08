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
<html>
    <head>
        <title>DACH DHBW</title>
        <meta charset="UTF-8">
        <meta name="author" charset="Dirk Hattemer, Alexander Müller">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="/style.css">
        <script src="https://kit.fontawesome.com/yourcode.js"></script>
    </head>
    <body>
        <header class="main-header">
            <div class="main-header-center">
                <div class="main-header-nav-icon">
                    <span onclick="openNav()">&#9776;</span>
                </div>
                <div class="main-header-img">
                    <img src="/media/DACH_logo.png" width="200px" height="auto">
                </div>
            </div>
        </header>
        <nav id="topNav" class="overlay-nav">
            <div class="overlay-nav-content">
                <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                <a class="active" href="#home">Home</a>
                <a href="#history">Historie</a>
                <a href="#profil">Profil</a>
                <a href="#about">About</a>
                <a href="/index.html">Logout</a>
            </div>
        </nav>
        <div class="test">
            <section class="main">
                <section class="main-section">
                    <atricle>
                        <header>
                            <h1>Corona Infektion Melden</h1>
                        </header>
                        <main>
                            <h2>Bestätigen Sie hier dass sie Infiziert sind:</h2>
                            <form method="post" action="/scripts/main.py">
                                <input type="hidden" id="ident" name="ident" value={ident_value}>
                                <input type="hidden" id="next_param" name="next_param" value={INFECTION_CONFIRMED}>
                                <button type="submit">Ja. Ich bin infiziert</button>
                            </form>
                        </main>
                    </atricle>
                </section>
                <section class="aside-section">
                    <aside>
                        <h1>Seitenleiste</h1>
                    </aside>
                    <aside>
                        <!-- das werden Lernvorschlage -->
                    </aside>
                    <aside>
                        <!-- hier könnte eine Werbeanzeige stehen -->
                    </aside>
                </section>
            </section>
        </div>
        <footer>
            <nav>
                <div>
                    <ul class="footer-nav">
                        <li>&copy;DACH</li>
                        <li><a href="/impressum.html">Impressum</a></li>
                        <li><a href="/erklaerung.html">Datenschutzerklärung</a></li>
                    </ul>
                </div>
            </nav>
            <address>
            </address>
        </footer>
        <script>
            function openNav() ^
                document.getElementById("topNav").style.width = "100%";
            ~

            function closeNav() ^
                document.getElementById("topNav").style.width = "0%";
            ~
        </script>
    </body>
</html>
"""

    output = output.replace("^", "{")
    output = output.replace("~", "}")

    print(output)

    #TODO Hash the ident; store in extra db table; not to pretty but should be alright

    return


def change_covid_state_infected(data_array):
    """
    Change all the Corona States after a reported Infection.
    param: {array} data_array; Input Data, here only ident interesting
    """

    #TODO ident still holds the email, future it should hold a hash value that is linked to a user in a different table
    #TODO therefore must this query be changed in the future!

    #TODO trys/ecxepts with own error codes and Messages!

    DATA_HANDLE[0].execute(f"""UPDATE user SET covid_state = {INFECTED} WHERE email LIKE '{data_array[0][1]}'""")


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
        (date >= CURDATE() - INTERVAL {LOWER_LIMIT} DAY) AND (date < CURDATE() - INTERVAL {UPPER_LIMIT} DAY) AND
        ((begin <= '{infected_begin}' AND end <= '{infected_end}' AND end >= '{infected_begin}') OR (begin >= '{infected_begin}' AND end >= '{infected_end}' AND begin <= '{infected_end}') OR
        (begin >= '{infected_begin}' AND end <= '{infected_end}') OR (begin <= '{infected_begin}' AND end >= '{infected_end}'))""")

        low_risk_person = DATA_HANDLE[0].fetchall()
        for i in range(0, len(low_risk_person)):
            low_risk_ids.append(low_risk_person[i][0])

        #Get high risk persons and save them
        DATA_HANDLE[0].execute(f"""SELECT person FROM movement WHERE person != {infected_id} AND room = {result[i][0]} AND date = '{result[i][1]}' AND 
        (date >= CURDATE() - INTERVAL {UPPER_LIMIT} DAY) AND
        ((begin <= '{infected_begin}' AND end <= '{infected_end}' AND end >= '{infected_begin}') OR (begin >= '{infected_begin}' AND end >= '{infected_end}' AND begin <= '{infected_end}') OR
        (begin >= '{infected_begin}' AND end <= '{infected_end}') OR (begin <= '{infected_begin}' AND end >= '{infected_end}'))""")

        high_risk_person = DATA_HANDLE[0].fetchall()
        for i in range(0, len(high_risk_person)):
            high_risk_ids.append(high_risk_person[i][0])
        

    #Set the accroding covid_states
    for i in range(0, len(low_risk_ids)):
        DATA_HANDLE[0].execute(f"""UPDATE user SET covid_state = {LOW_RISK} WHERE uid = {low_risk_ids[i]}""")

    for i in range(0, len(high_risk_ids)):
        DATA_HANDLE[0].execute(f"""UPDATE user SET covid_state = {HIGH_RISK} WHERE uid = {high_risk_ids[i]}""")

    return