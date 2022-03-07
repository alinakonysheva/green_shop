import sys
from myapp import create_app

sys.dont_write_bytecode = True

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, flash, redirect, url_for, abort, request
from config import DB_HOST, DB_PASSWORD, DB_USER_NAME, DB_PORT, DB_NAME
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Een “webshop” maken. In onze webshop verkopen we boeken, zowel fysieke als audio als voor een e reader.
# Elk boek heeft uiteraard een paar eigenschappen. Elke klant heeft uiteraard ook een paar eigenschappen
# Wat moet er gemaakt worden:
# - een klantenbestand
#  - product pagina(’s)
#  - gemakkelijke filters op product
#  - login/wachtwoord reset
#  - een wenslijst van een klant, een klant kan dus een boek op zijn wenslijst zetten en uiteraard daar
# ook afhalen
# Note: het is niet de bedoeling dat we een betaal en/of facturatie systeem en dergelijke gaan toevoegen.
# Ook geen shopping cart

# export FLASK_ENV=development -- если исправляю ошибки в шаблонах
# если хочу протестировать error handling FLASK_ENV=production


"""@app.errorhandler(404)
def do_not_found_error(error):
    return render_template(), 404
"""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


def do_run():
    from database import create_database, engine, session
    create_database(engine, do_erase=True)

    """eb = EBook()
    eb.size = 25
    eb.book_title = 'Ebook_1'
    eb.author_first_name = 'author'
    eb.language = 'af'
    eb.category = 2
    eb.publisher = 'alpina'
    eb.release_year = 2000
    eb.rating = 5
    eb.annotation = 'annotation to the Ebook_1 of author'
    eb.author_last_name = 'lastnameauthor'
    eb.author_middle_name = 'middlenameauthor'
    session.add(eb)
    session.commit()"""


if __name__ == '__main__':
    do_run()
