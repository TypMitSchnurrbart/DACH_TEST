#!/usr/bin/python3
#!-*- coding: utf-8 -*-


def show_index_html():

    print("""
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
                        <li><a href="../impressum.html">Impressum</a></li>
                        <li><a href="../erklaerung.html">Datenschutzerklärung</a></li>
                    </ul>
                </div>
            </nav>
            <address>
            </address>
        </footer>""")

    return