#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.get_data import get_user_data, get_user_id, get_last_room, get_visited_rooms, get_number_of_users
from files.const import VORNAME, NACHNAME, COVID_STATE, REPORT_INFECTION, VERSION, LAST_UPDATE
from files.error_handle import translate_covid_state

def show_homepage(data_array):
    """
    Displaying the Body of the Home Page
    param:  {list}  data_array; Containing the QueryString Information
    """

    #Get the uid from the current user
    activ_uid = get_user_id(data_array)

    #Get some data to display initialy
    vorname, nachname, covid_state = get_user_data(activ_uid, VORNAME, NACHNAME, COVID_STATE)
    covid_state = translate_covid_state(covid_state)

    #Returns a String containing last room
    last_room = get_last_room(activ_uid)

    #Returns array like this: [(room, date, begin, end), (room, date, ....)] newest room with lowest index!
    last_rooms_array = get_visited_rooms(activ_uid)

    #Getting active user amount
    number_of_users = get_number_of_users()

    #TODO Like this only for test; Ident should be the email but hashed
    ident_value = data_array[0][1]

    output = f"""<!DOCTYPE html>
    <html lang="de">
        <head>
            <title>DACH DHBW - Startseite</title>
            <meta charset="UTF-8">
            <meta name="author" charset="Dirk Hattemer, Alexander Müller, Tim Fassbender">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <script src="https://kit.fontawesome.com/672bee8847.js" crossorigin="anonymous"></script>
            <link rel="stylesheet" href="/style.css">
        </head> 
        <body>
            <nav id="topNav" class="overlay-nav">
                <div class="overlay-nav-content">
                    <a href="javascript:void(0)" class="closebtn" id="closeNav">&times;</a>
                    <a class="active" href="/HTML/dashboard.html">Dashboard</a>
                    <a href="">Raumverlauf</a>
                    <a href="/index.html">Logout</a>
                    <a href="">...</a>
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
                    <h1 class="title">Dashboard</h1>
                    <h3>Willkommen {vorname} {nachname}!</h3>
                    <div class="dash-cards">
                        <div class="card-single">
                            <div class="card-footer">
                                <a href="">Weitere Info´s</a>
                            </div>
                            <div class="card-body">
                                <span class="fas fa-virus"></span>
                                <div>
                                    <h5>Statusmeldung</h5>
                                    <h4 id="state">Status: {covid_state}!</h4>
                                </div>
                            </div>
                        </div>
                        <div class="card-single">
                            <div class="card-footer">
                                <a href="">Gesamter Verlauf</a>
                            </div>
                            <div class="card-body">
                                <span class="fas fa-home"></span>
                                <div>
                                    <h5>Letzter / Aktiver</h5>
                                    <h4 id="lastR">Raum: ---</h4>
                                </div>
                            </div>
                        </div>
                        <div class="card-single">
                            <div class="card-footer">
                                <a href="">Weitere Info´s</a>
                            </div>
                            <div class="card-body">
                                <span class="fas fa-briefcase-medical"></span>
                                <div>
                                    <h5>Krankmelden</h5>
                                    <h4>
                                        <form method="post" action="/scripts/main.py">
                                            <input type="hidden" id="ident" name="ident" value={ident_value}>
                                            <input type="hidden" id="next_param" name="next_param" value={REPORT_INFECTION}>
                                            <button type="submit" class="btnKrank">Melden sie sich krank!</button>
                                        </form>
                                    </h4>
                                </div>
                            </div>
                        </div>
                        <div class="card-single">
                            <div class="card-footer">
                                <a href="">Profil bearbeiten</a>
                            </div>
                            <div class="card-body">
                                <span class="fas fa-user-cog"></span>
                                <div>
                                    <h5>Einstellungen</h5>
                                    <h4>Profil</h4>
                                </div>
                            </div>
                        </div>
                    </div>
                    <section class="recent">
                        <div class="activity-grid">
                            <div class="room-card">
                                <h3>Raumverlauf</h3>
                                <div class="table-responsive">
                                    <table>
                                        <thead>
                                            <tr>
                                                <th>Raum</th>
                                                <th>Datum</th>
                                                <th>Anfang</th>
                                                <th>Ende</th>
                                            </tr>
                                        </thead>
                                        <tbody id="tabelle">"""

    #Print First Half of output
    print(output)

    #Get the table done
    if (last_rooms_array[0] == "$false$"):
        print(f"""                          <tr>
                                                 <td>Kein Raum in den letzten 14 Tagen!</td>
                                                 <td></td>
                                                 <td></td>
                                                 <td></td>
                                             </tr>
                 """)
    else: 
        for i in range(0, len(last_rooms_array)):
            print(f"""                          <tr>
                                                         <td>{last_rooms_array[i][0]}</td>
                                                         <td>{last_rooms_array[i][1]}</td>
                                                         <td>{last_rooms_array[i][2]} Uhr</td>
                                                         <td>{last_rooms_array[i][3]} Uhr</td>
                                                     </tr>
                         """)

    #Define second half of output
    output = f"""                            
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div class="summary">
                                <div class="summary-card">
                                    <div class="summary-single">
                                        <span class="far fa-id-badge"></span>
                                        <div>
                                            <h5>{number_of_users}</h5>
                                            <small>Aktive Nutzer</small>
                                        </div>
                                    </div>
                                    <div class="summary-single">
                                        <span class="fas fa-calendar-week"></span>
                                        <div>
                                            <h5>{LAST_UPDATE}</h5>
                                            <small>Letztes Update</small>
                                        </div>
                                    </div>
                                    <div class="summary-single">
                                        <span class="fas fa-code-branch"></span>
                                        <div>
                                            <h5>{VERSION}</h5>
                                            <small>Version</small>
                                        </div>
                                    </div>
                                </div>
                            </div>
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
                <script src="/JavaScript/index.js"></script>
                <script src="/JavaScript/dashboard.js"></script>
            </div>
        </body>
    </html>
    """

    #Print second Half of Output
    print(output)

    return