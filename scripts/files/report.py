#!/usr/bin/python3
#! -*- coding: utf-8 -*-

from files.const import INFECTION_CONFIRMED, DATA_HANDLE

def show_report_page(data_array):

    #TODO This is just for testing like this!
    ident_value = data_array[0][1]

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


def change_covid_states(data_array):
    """
    Change all the Corona States after a reported Infection.
    param: {array} data_array; Input Data, here only ident interesting
    """

    #TODO Change the risk states; for now only changing own state to 4
    #TODO ident still holds the email, future it should hold a hash value that is linked to a user in a different table
    #TODO therefore must this query be changed in the future!

    #TODO try/ecxept with own error code and Message!
    DATA_HANDLE[0].execute(f"""UPDATE user SET covid_state = 4 WHERE email LIKE '{data_array[0][1]}'""")

    return