#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.database import get_user_data
from files.const import VORNAME, NACHNAME, COVID_STATE
from files.error_handle import translate_covid_state

def show_homepage(data_array):
    """
    Displaying the Body of the Home Page
    param:  {list}  data_array; Containing the QueryString Information
    """

    vorname, nachname, covid_state = get_user_data(data_array, VORNAME, NACHNAME, COVID_STATE)
    covid_state = translate_covid_state(covid_state)

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
                <a href="/move_test.html">MOVE_TEST</a>
            </div>
        </nav>
        <div class="test">
            <section class="main">
                <section class="main-section">
                    <atricle>
                        <header>
                            <h1>Willkommen {vorname} {nachname} !</h1>
                        </header>
                        <main>
                            Ihr Corona-Status ist: {covid_state}!
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

    #TODO Delete MOVE_Test from sidenav
    #TODO Create own Covid-State Query to translate id to string for output
    return