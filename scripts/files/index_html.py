#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.error_handle import get_error_text


def show_index_html(error_code):

    error_text = ""

    if error_code != None:
        result = get_error_text(error_code)
        error_text = result

    #In this Page the Path to the Files are to be aware of! with /<file> it starts from the root of the webserver!
    print(f"""
     <header>
            <h1>DACH - Deine Bewegung in der Hochschule!</h1>
        </header>

        <section>
            <section>
                <atricle>
                    <header>
                        <h1>Login</h1>
                    </header>
                    <main>
                        <form action="/scripts/main.py" target="_self" autocomplete="on" method="post">
                            <fieldset>
                                <label for="email">E-Mail:</label><br>
                                <input type="email" id="email" name="email"><br>
                                <label for="password">Passwort:</label><br>
                                <input type="password" id="password" name="password"><br>
                                <input type="hidden" id="next_param" name="next_param" value="from_index_html"><br>
                                <input type="submit" value="Absenden">
                            </fieldset>
                        </form>
                    </main>
                </atricle>
                <p>{error_text}<p>
            </section>
            <section>
                <aside>
                    <br>
                    <form action="/register.html">
                        <input type="submit" value="Neu? Hier registrieren!" />
                    </form>
                </aside>
                <aside>
                    <!-- das wird eine Suche -->
                </aside>
                <aside>
                    <!-- das werden Lernvorschlage -->
                </aside>
                <aside>
                    <!-- hier könnte eine Werbeanzeige stehen -->
                </aside>
            </section>
        </section>

        <footer>
            <p></p>
            <nav>
                <div>
                    <ul class="fmenu">
                        <li>&copy;DACH</li>
                        <li><a href="/impressum.html">Impressum</a></li>
                        <li><a href="/erklaerung.html">Datenschutzerklärung</a></li>
                    </ul>
                </div>
            </nav>
            <address>
            </address>
        </footer>""")

    return