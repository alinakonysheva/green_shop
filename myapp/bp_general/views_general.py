from flask import render_template, abort, redirect, flash, url_for, current_app, Blueprint

from bp_general.form_books import EbookForm, AudiobookForm, PaperbookForm
from myapp import db
from bp_general.controller_general import ControllerBook, ControllerEBook, ControllerAudioBook, ControllerPaperBook

bp_general_app = Blueprint('bp_general', __name__, cli_group="db")


@bp_general_app.route('/')
def do_home():
    controller = ControllerBook(db.session)
    return render_template('general/home.html', name='some name', ids=controller.get_all_ids())


@bp_general_app.route('/books')
def do_books():
    ebooks = ControllerEBook(db.session).get_all_ebook()
    audiobooks = ControllerAudioBook(db.session).get_all_audiobook()
    paperbooks = ControllerPaperBook(db.session).get_all_paper_book()
    books = ebooks + audiobooks + paperbooks

    return render_template('general/books.html', books=books)


@bp_general_app.route('/books/addebook')
def add_ebook():
    return render_template('general/addebook.html', form=EbookForm())


@bp_general_app.route('/books/addaudiobook')
def add_audiobook():
    return render_template('general/addaudiobook.html', form=AudiobookForm())


@bp_general_app.route('/books/addpaperbook')
def add_paper_book():
    return render_template('general/addpaperbook.html', form=PaperbookForm())


@bp_general_app.route('/books/ebook/delete/<int:ebook_id>')
def delete_ebook(ebook_id):
    ControllerEBook(db.session).remove_ebook(ebook_id)
    return redirect(url_for('bp_general.do_books'))


@bp_general_app.route('/books/audiobook/delete/<int:audiobook_id>')
def delete_audiobook(audiobook_id):
    ControllerAudioBook(db.session).remove_audiobook(audiobook_id)
    return redirect(url_for('bp_general.do_books'))


@bp_general_app.route('/books/paperbook/delete/<int:paperbook_id>')
def delete_paperbook(paperbook_id):
    ControllerPaperBook(db.session).remove_paper_book(paperbook_id)
    return redirect(url_for('bp_general.do_books'))


@bp_general_app.route('/books/addebook', methods=['POST'])
def add_ebook_post():
    form = EbookForm()
    if form.validate_on_submit():
        controller = ControllerEBook(db.session)

        ebook = controller.add_ebook(form.title.data, form.size.data, form.author_first_name.data,
                                     form.author_middle_name.data, form.author_last_name.data,
                                     form.release_year.data, form.category.data, form.language.data,
                                     form.annotation.data, form.publisher.data, form.rating.data, form.pic.data)

        return redirect(url_for('bp_general.do_books'))
    else:
        abort(500)


# audiobook

@bp_general_app.route('/books/addaudiobook', methods=['POST'])
def add_audiobook_post():
    form = AudiobookForm()
    if form.validate_on_submit():
        controller = ControllerAudioBook(db.session)

        audiobook = controller.add_audiobook(form.title.data, form.reader_first_name.data, form.reader_last_name.data,
                                             form.reader_middle_name.data, form.duration_hours.data,
                                             form.duration_minutes.data,
                                             form.duration_seconds.data, form.author_first_name.data,
                                             form.author_middle_name.data, form.author_last_name.data,
                                             form.release_year.data, form.category.data, form.language.data,
                                             form.annotation.data, form.publisher.data, form.rating.data, form.pic.data)

        return redirect(url_for('bp_general.do_books'))
    else:
        abort(500)


@bp_general_app.route('/books/addpaperbook', methods=['POST'])
def add_paperbook_post():
    form = PaperbookForm()
    if form.validate_on_submit():
        controller = ControllerPaperBook(db.session)

        paperbook = controller.add_paper_book(form.title.data, form.cover.data, form.length.data, form.width.data,
                                              form.weight.data, form.pages.data, form.isbn.data,
                                              form.author_first_name.data,
                                              form.author_middle_name.data, form.author_last_name.data,
                                              form.release_year.data, form.category.data, form.language.data,
                                              form.annotation.data, form.publisher.data, form.rating.data,
                                              form.pic.data)

        return redirect(url_for('bp_general.do_books'))
    else:
        abort(500)


def do_not_found(error):
    return render_template('general/errors.html', code=404, error=error)


def do_not_authorized(error):
    return render_template('general/errors.html', code=403, error=error)


def do_server_error(error):
    return render_template('general/errors.html', code=500, error=error)
