#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.error_handle import get_error_text


def show_index_html(error_code):

    error_text = ""

    if error_code != None:
        result = get_error_text(error_code)
        error_text = result[0][1]

    #In this Page the Path to the Files are to be aware of! with /<file> it starts from the root of the webserver!
    print("""<!DOCTYPE html>
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
                <a href="#room">Räume</a>
                <a href="#history">Historie</a>
                <a href="#profil">Profil</a>
                <a href="#about">About</a>
            </div>
        </nav>
        <div class="test">
            <section class="main">
                <section class="main-section">
                    <atricle>
                        <header>
                            <h1>Login</h1>
                        </header>
                        <main>
                            <div class="container-form">
                                <form action="/scripts/main.py" target="_self" autocomplete="on" method="post">
                                    <div class="row">
                                        <div class="col-25">
                                            <label for="email">E-Mail:</label>
                                        </div>
                                        <div class="col-75">
                                            <input type="email" id="email" name="email">
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-25">
                                            <label for="password">Passwort:</label>
                                        </div>
                                        <div class="col-75">
                                            <input type="password" id="password" name="password">
                                        </div>
                                        <div class="row">
                                            <input type="hidden" id="next_param" name="next_param" value="from_index_html"><br>
                                            <input type="submit" value="Absenden">
                                        </div>
                                    </div>
                                </form>
                                <form action="/register.html">
                                    <input type="submit" value="Neu? Hier registrieren!" />
                                </form>
                            </div>
                        </main>
                    </atricle>
                    <h2>%s</h2>
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
            function openNav() {
                document.getElementById("topNav").style.width = "100%";
            }

            function closeNav() {
                document.getElementById("topNav").style.width = "0%";
            }
        </script>
    </body>
</html>
""" %(error_text))

    return