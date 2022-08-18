import os
import uuid

from flask import render_template, abort, redirect, flash, url_for, Blueprint, request, send_from_directory

from myapp.bp_general.form_books import EbookForm, AudiobookForm, PaperbookForm, SearchForm
from myapp import db
from myapp.bp_general.controller_general import ControllerBook, ControllerEBook, ControllerAudioBook, ControllerPaperBook, \
    ControllerWishlist, ControllerUsers
from werkzeug.utils import secure_filename

bp_general_app = Blueprint('bp_general', __name__, cli_group="db")

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@bp_general_app.route('/home')
def do_home():
    controller = ControllerBook(db.session)
    return render_template('general/home.html', name='some name', ids=controller.get_all_ids(), form=SearchForm())


@bp_general_app.route('/books')
def do_books():
    ebooks = ControllerEBook(db.session).get_all_ebook()
    audiobooks = ControllerAudioBook(db.session).get_all_audiobook()
    paperbooks = ControllerPaperBook(db.session).get_all_paper_book()
    books = ebooks + audiobooks + paperbooks

    return render_template('general/books.html', books=books)


@bp_general_app.route('/books/book_details/<int:book_id>')
def show_book(book_id):
    book = ControllerPaperBook(db.session).get_paper_book_by_id(book_id) or ControllerAudioBook(
        db.session).get_audiobook_by_id(book_id) or ControllerEBook(db.session).get_ebook_by_id(book_id)
    if book:

        return render_template('general/viewbook.html', book=book)
    else:
        return redirect(url_for('bp_general.do_books'))


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
    flash('Book was deleted from data base', 'OK')
    return redirect(url_for('bp_general.do_books'))


@bp_general_app.route('/books/audiobook/delete/<int:audiobook_id>')
def delete_audiobook(audiobook_id):
    ControllerAudioBook(db.session).remove_audiobook(audiobook_id)
    flash('Book was deleted from data base', 'OK')
    return redirect(url_for('bp_general.do_books'))


@bp_general_app.route('/books/paperbook/delete/<int:paperbook_id>')
def delete_paperbook(paperbook_id):
    ControllerPaperBook(db.session).remove_paper_book(paperbook_id)
    flash('Book was deleted from data base', 'OK')
    return redirect(url_for('bp_general.do_books'))


@bp_general_app.route('/books/add_to_wishlist/<int:book_id>')
def add_book_to_wishlist(book_id):
    controller_wishlist = ControllerWishlist(db.session)
    wl_id = controller_wishlist.get_wishlist_by_user(ControllerUsers(db.session).get_current_user().id).id
    controller_wishlist.add_book_to_wishlist(wl_id, book_id)
    flash('Book was added to your Wishlist', 'OK')
    return redirect(url_for('bp_general.do_books'))


# to edit books
@bp_general_app.route('/books/changeebook/<int:book_id>')
def change_ebook(book_id):
    controller = ControllerEBook(db.session)
    ebook = controller.get_ebook_by_id(book_id)
    ebookform = EbookForm()
    ebookform.title.data = ebook.book_title
    ebookform.author_first_name.data = ebook.author_first_name
    ebookform.author_last_name.data = ebook.author_last_name
    ebookform.author_middle_name.data = ebook.author_middle_name
    ebookform.release_year.data = ebook.release_year
    ebookform.rating.data = ebook.rating
    ebookform.pic.data = ebook.pic
    ebookform.category.data = ebook.category
    ebookform.language.data = ebook.language
    ebookform.annotation.data = ebook.annotation
    ebookform.publisher.data = ebook.publisher
    ebookform.size.data = ebook.size

    return render_template('general/changeebook.html', form=ebookform, book=ebook)


@bp_general_app.route('/books/changeaudiobook/<int:book_id>')
def change_audiobook(book_id):
    controller = ControllerAudioBook(db.session)
    audiobook = controller.get_audiobook_by_id(book_id)
    audiobookform = AudiobookForm()
    audiobookform.title.data = audiobook.book_title
    audiobookform.author_first_name.data = audiobook.author_first_name
    audiobookform.author_last_name.data = audiobook.author_last_name
    audiobookform.author_middle_name.data = audiobook.author_middle_name
    audiobookform.release_year.data = audiobook.release_year
    audiobookform.rating.data = audiobook.rating
    audiobookform.pic.data = audiobook.pic
    audiobookform.category.data = audiobook.category
    audiobookform.language.data = audiobook.language
    audiobookform.annotation.data = audiobook.annotation
    audiobookform.publisher.data = audiobook.publisher
    audiobookform.reader_first_name.data = audiobook.reader_first_name
    audiobookform.reader_last_name.data = audiobook.reader_last_name
    audiobookform.reader_middle_name.data = audiobook.reader_middle_name
    audiobookform.duration_hours.data = audiobook.duration_hours
    audiobookform.duration_minutes.data = audiobook.duration_minutes
    audiobookform.duration_seconds.data = audiobook.duration_seconds
    return render_template('general/changeaudiobook.html', form=audiobookform, book=audiobook)


@bp_general_app.route('/books/changepaperbook/<int:book_id>')
def change_paperbook(book_id):
    controller = ControllerPaperBook(db.session)
    paper_book = controller.get_paper_book_by_id(book_id)
    paperbookform = PaperbookForm()
    paperbookform.title.data = paper_book.book_title
    paperbookform.author_first_name.data = paper_book.author_first_name
    paperbookform.author_last_name.data = paper_book.author_last_name
    paperbookform.author_middle_name.data = paper_book.author_middle_name
    paperbookform.release_year.data = paper_book.release_year
    paperbookform.rating.data = paper_book.rating
    paperbookform.pic.data = paper_book.pic
    paperbookform.category.data = paper_book.category
    paperbookform.language.data = paper_book.language
    paperbookform.annotation.data = paper_book.annotation
    paperbookform.publisher.data = paper_book.publisher
    paperbookform.pages.data = paper_book.pages
    paperbookform.cover.data = paper_book.cover
    paperbookform.isbn.data = paper_book.isbn
    paperbookform.weight.data = paper_book.weight
    paperbookform.length.data = paper_book.length
    paperbookform.width.data = paper_book.width
    return render_template('general/changepaperbook.html', form=paperbookform, book=paper_book)


@bp_general_app.route('/books/changeebook/<int:book_id>', methods=['POST', 'GET'])
def change_ebook_post(book_id):
    controller = ControllerEBook(db.session)
    form = EbookForm()
    if form.validate_on_submit():
        ebook = controller.change_ebook(book_id, form.title.data, form.size.data, form.author_first_name.data,
                                        form.author_middle_name.data, form.author_last_name.data,
                                        form.release_year.data, form.category.data, form.language.data,
                                        form.annotation.data, form.publisher.data, form.rating.data, form.pic.data)
        if ebook:
            flash('Book was changed in data base', 'OK')
        else:
            flash('Entered information was incorrect', 'ERROR')
        return render_template('general/viewbook.html', book=ebook)


# audiobook

@bp_general_app.route('/books/changeaudiobook/<int:book_id>', methods=['POST', 'GET'])
def change_audiobook_post(book_id):
    controller = ControllerAudioBook(db.session)
    form = AudiobookForm()
    if form.validate_on_submit():
        audiobook = controller.change_audiobook(book_id, form.title.data, form.reader_first_name.data,
                                                form.reader_last_name.data,
                                                form.reader_middle_name.data, form.duration_hours.data,
                                                form.duration_minutes.data,
                                                form.duration_seconds.data, form.author_first_name.data,
                                                form.author_middle_name.data, form.author_last_name.data,
                                                form.release_year.data, form.category.data, form.language.data,
                                                form.annotation.data, form.publisher.data, form.rating.data,
                                                form.pic.data)
        if audiobook:
            flash('Book was changed in data base', 'OK')
            return render_template('general/viewbook.html', book=audiobook)
        else:
            flash('Entered information was incorrect', 'ERROR')
            return redirect(url_for('bp_general.do_books'))

    else:
        abort(500)


@bp_general_app.route('/books/changepaperbook/<int:book_id>', methods=['POST', 'GET'])
def change_paperbook_post(book_id):
    form = PaperbookForm()
    controller = ControllerPaperBook(db.session)
    if form.validate_on_submit():
        paperbook = controller.change_paper_book(book_id, form.title.data, form.cover.data, form.length.data,
                                                 form.width.data, form.weight.data, form.pages.data,
                                                 form.isbn.data,
                                                 form.author_first_name.data, form.author_middle_name.data,
                                                 form.author_last_name.data, form.release_year.data, form.category.data,
                                                 form.language.data, form.annotation.data, form.publisher.data,
                                                 form.rating.data, form.pic.data)
        if paperbook:
            flash('Book was changed in data base', 'OK')
        else:
            flash('Entered information was incorrect', 'ERROR')
        return render_template('general/viewbook.html', book=paperbook)
    else:
        abort(500)


# end edit
@bp_general_app.route('/books/addebook', methods=['POST'])
def add_ebook_post():
    form = EbookForm()
    if form.validate_on_submit():
        controller = ControllerEBook(db.session)
        ebook = controller.add_ebook(form.title.data, form.size.data, form.author_first_name.data,
                                     form.author_middle_name.data, form.author_last_name.data,
                                     form.release_year.data, form.category.data, form.language.data,
                                     form.annotation.data, form.publisher.data, form.rating.data, form.pic.data)
        flash('Book was added in data base', 'OK')
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
        flash('Book was added in data base', 'OK')
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
        flash('Book was added in data base', 'OK')
        return redirect(url_for('bp_general.do_books'))
    else:
        abort(500)


@bp_general_app.route('/searchpaperbook', methods=['POST'])
def find_book():
    form = SearchForm()
    if form.validate_on_submit():
        controller_p = ControllerPaperBook(db.session)
        books_p = controller_p.get_by_filter(form)
        controller_p = ControllerAudioBook(db.session)
        books_a = controller_p.get_by_filter(form)
        controller_p = ControllerEBook(db.session)
        books_e = controller_p.get_by_filter(form)

        books = books_p + books_a + books_e

        return render_template('general/books.html', books=books)
    else:
        abort(500)


@bp_general_app.route('/wishlist')
def do_wishlist():
    user_controller = ControllerUsers(db.session)
    user = user_controller.get_current_user()
    controller = ControllerWishlist(db.session)
    wl = controller.get_wishlist_by_user(user.id)
    wishlist_books = wl.books
    html = render_template('general/wishlist.html', wishlist_books=wishlist_books)
    return html


@bp_general_app.route('/books/remove_from_wishlist/<int:wishlist_book_id>')
def delete_book_from_wishlist(wishlist_book_id):
    controller_wishlist = ControllerWishlist(db.session)
    controller_wishlist.delete_book_from_wishlist(wishlist_book_id)
    return redirect(url_for('bp_general.do_wishlist'))


def do_not_found(error):
    return render_template('general/errors.html', code=404, error=error)


def do_not_authorized(error):
    return render_template('general/errors.html', code=403, error=error)


def do_server_error(error):
    return render_template('general/errors.html', code=500, error=error)
