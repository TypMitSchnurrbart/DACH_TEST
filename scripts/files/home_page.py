#!/usr/bin/python3
#!-*- coding: utf-8 -*-


def show_homepage(data_array):
    """
    Displaying the Body of the Home Page
    param:  {list}  data_array; Containing the QueryString Information
    """

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
                            <h1>Überschrift</h1>
                        </header>
                        <main>
                            Inhalt
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
            function openNav() {
                document.getElementById("topNav").style.width = "100%";
            }

            function closeNav() {
                document.getElementById("topNav").style.width = "0%";
            }
        </script>
    </body>
</html>
""")

    return