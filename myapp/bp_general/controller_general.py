from datetime import datetime
from bp_general.constants import languages, categories, covers
from bp_general.modal_general import Book
from bp_general.modal_general import AudioBook
from bp_general.modal_general import EBook
from bp_general.modal_general import PaperBook


# TODO change all numbers to constants
# TODO in errors add input in f strings

class ControllerBook:
    # get all existing ids
    def __init__(self, session):
        self.session = session

    def get_all_ids(self):
        """
        to get list of all existing id's
        :return: list of str(id)
        """
        id_list = list(map(lambda x: x.id, self.session.query(Book).all()))
        return id_list


class ControllerAudioBook:
    def __init__(self, session):
        self.session = session

    def add_audiobook(self, title, reader_first_name, reader_last_name, reader_middle_name, duration_hours,
                      duration_minutes, duration_seconds, author_first_name, author_middle_name, author_last_name,
                      release_year, category, language, annotation, publisher, rating, pic):

        audiobook = AudioBook()

        if type(title) == str and 0 < len(title) < 200:
            audiobook.book_title = title
        else:
            raise ValueError('Title should be a string and length between 1 and 200 symbols')

        if  0 < len(reader_first_name) < 100:
            audiobook.reader_first_name = str(reader_first_name)
        else:
            raise ValueError('First name of author should be a string and length between 1 and 100 symbols')

        if 0 < len(reader_last_name) < 100:
            audiobook.reader_last_name = str(reader_last_name)
        else:
            raise ValueError('Middle name of author should be a string and length between 1 and 100 symbols')

        if 0 < len(reader_middle_name) < 100:
            audiobook.reader_middle_name = str(reader_middle_name)
        else:
            raise ValueError('Middle name of author should be a string and length between 1 and 100 symbols')

        if type(duration_hours) == int and duration_hours >= 0:
            audiobook.duration_hours = duration_hours
        else:
            raise ValueError('duration hours of audio book should be an integer and >= 0')

        if type(duration_minutes) == int and 0 <= duration_minutes <= 59:
            audiobook.duration_minutes = duration_minutes
        else:
            raise ValueError('duration minutes of audio book should be an integer and between 0 and 59')

        if type(duration_seconds) == int and 0 <= duration_seconds <= 59:
            audiobook.duration_seconds = duration_seconds
        else:
            raise ValueError('duration seconds of audio book should be an integer and between 0 and 59')

        if type(pic) == str and 0 < len(title) < 400:
            audiobook.pic = pic
        else:
            raise ValueError('Picture link should be a string and length between 1 and 400 symbols')

        if type(rating) == float and 0 <= rating <= 10:
            audiobook.rating = rating
        else:
            raise ValueError('rating of a ebook should be a float and between 0 and 10')

        if type(publisher) == str and 0 < len(title) < 200:
            audiobook.publisher = publisher
        else:
            raise ValueError('publisher should be a string and length between 1 and 200 symbols')

        if type(annotation) == str:
            audiobook.annotation = annotation
        else:
            raise ValueError('publisher should be a string')

        if len(language) != 2:
            raise ValueError('Language should be set with 2 letters')
        if language in languages.keys():
            audiobook.language = language
        else:
            raise ValueError('Language should be set with 2 existing abbreviation letters')

        category_options = categories.keys()
        if category in category_options:
            audiobook.category = category
        else:
            raise ValueError(f'category should be in between {min(category_options)} and {max(category_options)}')

        if release_year <= 1457:
            raise ValueError('First printed book appeared in 1457 year')
        today_year = datetime.today().year
        if release_year > today_year:
            raise ValueError(f'Year should be less than {today_year}')
        audiobook.release_year = release_year

        if type(author_first_name) == str and 0 < len(author_first_name) < 100:
            audiobook.author_first_name = author_first_name
        else:
            raise ValueError('First name of author should be a string and length between 1 and 100 symbols')

        if type(author_middle_name) == str and 0 < len(author_middle_name) < 100:
            audiobook.author_middle_name = author_middle_name
        else:
            raise ValueError('Middle name of author should be a string and length between 1 and 100 symbols')

        if type(author_last_name) == str and 0 < len(author_last_name) < 100:
            audiobook.author_last_name = author_last_name
        else:
            raise ValueError('Last name of author should be a string and length between 1 and 100 symbols')

        self.session.add(audiobook)
        self.session.commit()
        return audiobook.id

    def change_audiobook(self, id_audiobook, title, reader_first_name, reader_last_name, reader_middle_name,
                         duration_hours, duration_minutes, duration_seconds, author_first_name, author_middle_name,
                         author_last_name, release_year, category, language, annotation, publisher, rating, pic):
        try:
            audiobook = self.session.query(AudioBook).get(id_audiobook)
            if audiobook:
                if type(title) == str and 0 < len(title) < 200:
                    audiobook.book_title = title
                else:
                    raise ValueError('Title should be a string and length between 1 and 200 symbols')

                if type(reader_first_name) == str and 0 < len(reader_first_name) < 100:
                    audiobook.reader_first_name = reader_first_name
                else:
                    raise ValueError('First name of author should be a string and length between 1 and 100 symbols')

                if type(reader_last_name) == str and 0 < len(reader_last_name) < 100:
                    audiobook.reader_last_name = reader_last_name
                else:
                    raise ValueError('Middle name of author should be a string and length between 1 and 100 symbols')

                if type(reader_middle_name) == str and 0 < len(reader_middle_name) < 100:
                    audiobook.reader_middle_name = reader_middle_name
                else:
                    raise ValueError('Last name of author should be a string and length between 1 and 100 symbols')

                if type(duration_hours) == int and duration_hours >= 0:
                    audiobook.duration_hours = duration_hours
                else:
                    raise ValueError('duration hours of audio book should be an integer and >= 0')

                if type(duration_minutes) == int and 0 <= duration_minutes <= 59:
                    audiobook.duration_minutes = duration_minutes
                else:
                    raise ValueError('duration minutes of audio book should be an integer and between 0 and 59')

                if type(duration_seconds) == int and 0 <= duration_seconds <= 59:
                    audiobook.duration_seconds = duration_seconds
                else:
                    raise ValueError('duration seconds of audio book should be an integer and between 0 and 59')

                if type(pic) == str and 0 < len(title) < 400:
                    audiobook.pic = pic
                else:
                    raise ValueError('Picture link should be a string and length between 1 and 400 symbols')

                if type(rating) == float and 0 <= rating <= 10:
                    audiobook.rating = rating
                else:
                    raise ValueError('rating of a ebook should be a float and between 0 and 10')

                if type(publisher) == str and 0 < len(title) < 200:
                    audiobook.publisher = publisher
                else:
                    raise ValueError('publisher should be a string and length between 1 and 200 symbols')

                if type(annotation) == str:
                    audiobook.annotation = annotation
                else:
                    raise ValueError('publisher should be a string')

                if len(language) != 2:
                    raise ValueError('Language should be set with 2 letters')
                if language in languages.keys():
                    audiobook.language = language
                else:
                    raise ValueError('Language should be set with 2 existing abbreviation letters')

                category_options = categories.keys()
                if category in category_options:
                    audiobook.category = category
                else:
                    raise ValueError(
                        f'category should be in between {min(category_options)} and {max(category_options)}')

                if release_year <= 1457:
                    raise ValueError('First printed book appeared in 1457 year')
                today_year = datetime.today().year
                if release_year > today_year:
                    raise ValueError(f'Year should be less than {today_year}')
                audiobook.release_year = release_year

                if type(author_first_name) == str and 0 < len(author_first_name) < 100:
                    audiobook.author_first_name = author_first_name
                else:
                    raise ValueError('First name of author should be a string and length between 1 and 100 symbols')

                if type(author_middle_name) == str and 0 < len(author_middle_name) < 100:
                    audiobook.author_middle_name = author_middle_name
                else:
                    raise ValueError('Middle name of author should be a string and length between 1 and 100 symbols')

                if type(author_last_name) == str and 0 < len(author_last_name) < 100:
                    audiobook.author_last_name = author_last_name
                else:
                    raise ValueError('Last name of author should be a string and length between 1 and 100 symbols')

                self.session.add(audiobook)
                self.session.commit()
            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print(e)

    def rate_audiobook(self, id_audiobook, rate):

        ab = self.session.query(AudioBook).get(id_audiobook)
        if ab:
            if type(rate) == float and 0 <= rate <= 10:
                ab.rating = rate
            else:
                raise ValueError('rating of a ebook should be a float and between 0 and 10')
        else:
            raise ValueError('Book with this ID does not exist in data base')

    def remove_audiobook(self, id_audiobook):
        ab = self.session.query(AudioBook).get(id_audiobook)
        if ab:
            self.session.delete(ab)
            self.session.commit()
        else:
            raise ValueError('Book with this ID does not exist in data base')

    def get_audiobook_by_id(self, id_audiobook):
        ab = self.session.query(AudioBook).get(id_audiobook)
        if ab:
            return ab
        else:
            raise ValueError('Book with this ID does not exist in data base')

    def get_all_audiobook(self):
        """
        to get list of audio_book
        :return: list of instances of Audiobook
        """
        ab_list = self.session.query(AudioBook).all()
        return ab_list

    def get_all_audiobook_newest_first(self):
        """
        to get list of audio_book from newest to oldest
        :return: list of instances of AudioBook
        """
        ab_list = self.session.query(AudioBook).order_by(AudioBook._release_year.desc()).all()
        return ab_list

    def get_all_audiobook_oldest_first(self):
        """
        to get list of audio_books from oldest to newest
        :return: list of instances of AudioBook
        """
        ab_list = self.session.query(AudioBook).order_by(AudioBook._release_year.asc()).all()
        return ab_list

    def get_audiobook_by_title(self, title):
        ab_list = self.session.query(AudioBook).filter(AudioBook._title.like(title)).all()
        return ab_list

    def get_audiobook_by_author_last_name(self, last_name):
        ab_list = self.session.query(AudioBook).filter(AudioBook._author_last_name.like(last_name)).all()
        return ab_list

    def get_audiobook_by_author_first_name(self, first_name):
        eb_list = self.session.query(AudioBook).filter(AudioBook._author_first_name.like(first_name)).all()
        return eb_list

    def get_audiobook_by_category(self, category):
        ab_list = self.session.query(AudioBook).filter(AudioBook._category == category).all()
        return ab_list

    def get_audiobook_by_reader_last_name(self, last_name):
        ab_list = self.session.query(AudioBook).filter(AudioBook._reader_last_name.like(last_name)).all()
        return ab_list

    def get_audiobook_by_publisher(self, publisher):
        ab_list = self.session.query(AudioBook).filter(AudioBook._publisher.like(publisher)).all()
        return ab_list

    def get_audiobook_by_rating(self, min_rating=0, max_rating=10):
        ab_list = self.session.query(AudioBook).filter(AudioBook._rating <= max_rating,
                                                       AudioBook._rating >= min_rating).all()
        return ab_list

    def get_audiobook_by_release_year(self, year):
        ab_list = self.session.query(AudioBook).filter(AudioBook._release_year == year).all()
        return ab_list


class ControllerEBook:

    def __init__(self, session):
        self.session = session

    def add_ebook(self, title, size, author_first_name, author_middle_name, author_last_name, release_year,
                  category, language, annotation, publisher, rating, pic):
        ebook = EBook()

        if type(title) == str and 0 < len(title) < 200:
            ebook.book_title = title
        else:
            raise ValueError('Title should be a string and length between 1 and 200 symbols')

        if type(size) == float:
            ebook.size = size
        else:
            raise ValueError('size of a ebook should be a float')

        if type(pic) == str and 0 < len(title) < 400:
            ebook.pic = pic
        else:
            raise ValueError('Picture link should be a string and length between 1 and 400 symbols')

        if type(rating) == float and 0 <= rating <= 10:
            ebook.rating = rating
        else:
            raise ValueError('rating of a ebook should be a float and between 0 and 10')

        if type(publisher) == str and 0 < len(title) < 200:
            ebook.publisher = publisher
        else:
            raise ValueError('publisher should be a string and length between 1 and 200 symbols')

        if type(annotation) == str:
            ebook.annotation = annotation
        else:
            raise ValueError('publisher should be a string')

        if len(language) != 2:
            raise ValueError('Language should be set with 2 letters')
        if language in languages.keys():
            ebook.language = language
        else:
            raise ValueError('Language should be set with 2 existing abbreviation letters')

        category_options = categories.keys()
        if category in category_options:
            ebook.category = category
        else:
            raise ValueError(f'category should be in between {min(category_options)} and {max(category_options)}')

        if release_year <= 1457:
            raise ValueError('First printed book appeared in 1457 year')
        today_year = datetime.today().year
        if release_year > today_year:
            raise ValueError(f'Year should be less than {today_year}')
        ebook.release_year = release_year

        if type(author_first_name) == str and 0 < len(author_first_name) < 100:
            ebook.author_first_name = author_first_name
        else:
            raise ValueError('First name of author should be a string and length between 1 and 100 symbols')

        if type(author_middle_name) == str and 0 < len(author_middle_name) < 100:
            ebook.author_middle_name = author_middle_name
        else:
            raise ValueError('Middle name of author should be a string and length between 1 and 100 symbols')

        if type(author_last_name) == str and 0 < len(author_last_name) < 100:
            ebook.author_last_name = author_last_name
        else:
            raise ValueError('Last name of author should be a string and length between 1 and 100 symbols')

        self.session.add(ebook)
        self.session.commit()
        return ebook.id

    def change_ebook(self, id_ebook, title, size, author_first_name, author_middle_name, author_last_name, release_year,
                     category, language, annotation, publisher, rating, pic) -> None:

        ebook = self.session.query(EBook).get(id_ebook)
        if ebook:
            if type(title) == str and 0 < len(title) < 200:
                ebook.book_title = title
            else:
                raise ValueError('Title should be a string and length between 1 and 200 symbols')

            if type(size) == float:
                ebook.size = size
            else:
                raise ValueError('size of a ebook should be a float')

            if type(pic) == str and 0 < len(title) < 400:
                ebook.pic = pic
            else:
                raise ValueError('Picture link should be a string and length between 1 and 400 symbols')

            if type(rating) == float and 0 <= rating <= 10:
                ebook.rating = rating
            else:
                raise ValueError('rating of a ebook should be a float and between 0 and 10')

            if type(publisher) == str and 0 < len(title) < 200:
                ebook.publisher = publisher
            else:
                raise ValueError('publisher should be a string and length between 1 and 200 symbols')

            if type(annotation) == str:
                ebook.annotation = annotation
            else:
                raise ValueError('publisher should be a string')

            if len(language) != 2:
                raise ValueError('Language should be set with 2 letters')
            if language in languages.keys():
                ebook.language = language
            else:
                raise ValueError('Language should be set with 2 existing abbreviation letters')

            category_options = categories.keys()
            if category in category_options:
                ebook.category = category
            else:
                raise ValueError(f'category should be in between {min(category_options)} and {max(category_options)}')

            if release_year <= 1457:
                raise ValueError('First printed book appeared in 1457 year')
            today_year = datetime.today().year
            if release_year > today_year:
                raise ValueError(f'Year should be less than {today_year}')
            ebook.release_year = release_year

            if type(author_first_name) == str and 0 < len(author_first_name) < 100:
                ebook.author_first_name = author_first_name
            else:
                raise ValueError('First name of author should be a string and length between 1 and 100 symbols')

            if type(author_middle_name) == str and 0 < len(author_middle_name) < 100:
                ebook.author_middle_name = author_middle_name
            else:
                raise ValueError('Middle name of author should be a string and length between 1 and 100 symbols')

            if type(author_last_name) == str and 0 < len(author_last_name) < 100:
                ebook.author_last_name = author_last_name
            else:
                raise ValueError('Last name of author should be a string and length between 1 and 100 symbols')

            self.session.add(ebook)
            self.session.commit()
        else:
            raise ValueError('Book with this ID does not exist in data base')

    def rate_ebook(self, id_ebook, rate):
        try:
            eb = self.session.query(EBook).get(id_ebook)
            if eb:
                if type(rate) == float and 0 <= rate <= 10:
                    eb.rating = rate
                else:
                    raise ValueError('rating of a ebook should be a float and between 0 and 10')
            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print('book was not rated: ', e)

    def remove_ebook(self, id_ebook):
        try:
            eb = self.session.query(EBook).get(id_ebook)
            if eb:
                self.session.delete(eb)
                self.session.commit()
            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print(e, 'this book does not exist')

    def get_ebook_by_id(self, id_ebook):
        eb = self.session.query(EBook).get(id_ebook)
        if eb:
            return eb
        else:
            raise ValueError('Book with this ID does not exist in data base')

    def get_all_ebook(self):
        """
        to get list of e-books
        :return: list of instances of EBook
        """
        eb_list = self.session.query(EBook).all()
        return eb_list

    def get_all_ebook_newest_first(self):
        """
        to get list of e-books from newest to oldest
        :return: list of instances of EBook
        """
        eb_list = self.session.query(EBook).order_by(EBook._release_year.desc()).all()
        return eb_list

    def get_all_ebook_oldest_first(self):
        """
        to get list of e-books from oldest to newest
        :return: list of instances of EBook
        """
        eb_list = self.session.query(EBook).order_by(EBook._release_year.asc()).all()
        return eb_list

    def get_ebook_by_title(self, title):
        eb_list = self.session.query(EBook).filter(EBook._title.like(f'%{title}%')).all()
        return eb_list

    def get_ebook_by_author_last_name(self, last_name):
        eb_list = self.session.query(EBook).filter(EBook._author_last_name.like(f'%{last_name}%')).all()
        return eb_list

    def get_ebook_by_author_first_name(self, first_name):
        eb_list = self.session.query(EBook).filter(EBook._author_first_name.like(f'%{first_name}%')).all()
        return eb_list

    def get_ebook_by_category(self, category):
        eb_list = self.session.query(EBook).filter(EBook._category == category).all()
        return eb_list

    def get_ebook_by_release_year(self, year):
        eb_list = self.session.query(EBook).filter(EBook._release_year == year).all()
        return eb_list

    def get_ebook_by_publisher(self, publisher):
        eb_list = self.session.query(EBook).filter(EBook._publisher.like(publisher)).all()
        return eb_list

    def get_ebook_by_rating(self, min_rating=0, max_rating=10):
        eb_list = self.session.query(EBook).filter(EBook._rating <= max_rating, EBook._rating >= min_rating).all()
        return eb_list


class ControllerPaperBook:

    def __init__(self, session):
        self.session = session

    def add_paper_book(self, title, cover, length, width, weight, pages, isbn, author_first_name, author_middle_name,
                       author_last_name, release_year, category, language, annotation, publisher, rating, pic):

        paper_book = PaperBook()

        if type(title) == str and 0 < len(title) < 200:
            paper_book.book_title = title
        else:
            raise ValueError('Title should be a string and length between 1 and 200 symbols')

        if cover in covers.keys():
            paper_book.cover = cover
        else:
            raise ValueError(f'Cover should be in {covers.keys()}')

        if 0 <= length <= 300:
            paper_book.length = length
        else:
            raise ValueError('length of a paper book should be a float and between 0 and 300')

        if 0 <= width <= 300:
            paper_book.width = width
        else:
            raise ValueError('width of a paper book should be a float and between 0 and 300')

        if 0 <= weight <= 10000:
            paper_book.weight = weight
        else:
            raise ValueError('weight of a paper book should be a float and between 0 and 10000')

        if type(pages) == int and 0 <= pages <= 23675:
            paper_book.pages = pages
        else:
            raise ValueError('pages of a paper book should be an int and between 0 and 23675')

        if len(isbn) == 13:
            paper_book.isbn = isbn
        else:
            raise ValueError('isbn of a paper book should be the number of digits with the length == 13')

        if type(pic) == str and 0 < len(title) < 400:
            paper_book.pic = pic
        else:
            raise ValueError('Picture link should be a string and length between 1 and 400 symbols')

        if type(rating) == float and 0 <= rating <= 10:
            paper_book.rating = rating
        else:
            raise ValueError('rating of a ebook should be a float and between 0 and 10')

        if type(publisher) == str and 0 < len(title) < 200:
            paper_book.publisher = publisher
        else:
            raise ValueError('publisher should be a string and length between 1 and 200 symbols')

        if type(annotation) == str:
            paper_book.annotation = annotation
        else:
            raise ValueError('publisher should be a string')

        if len(language) != 2:
            raise ValueError('Language should be set with 2 letters')
        if language in languages.keys():
            paper_book.language = language
        else:
            raise ValueError('Language should be set with 2 existing abbreviation letters')

        category_options = categories.keys()
        if category in category_options:
            paper_book.category = category
        else:
            raise ValueError(f'category should be in between {min(category_options)} and {max(category_options)}')

        if release_year <= 1457:
            raise ValueError('First printed book appeared in 1457 year')
        today_year = datetime.today().year
        if release_year > today_year:
            raise ValueError(f'Year should be less than {today_year}')
        paper_book.release_year = release_year

        if type(author_first_name) == str and 0 < len(author_first_name) < 100:
            paper_book.author_first_name = author_first_name
        else:
            raise ValueError('First name of author should be a string and length between 1 and 100 symbols')

        if type(author_middle_name) == str and 0 < len(author_middle_name) < 100:
            paper_book.author_middle_name = author_middle_name
        else:
            raise ValueError('Middle name of author should be a string and length between 1 and 100 symbols')

        if type(author_last_name) == str and 0 < len(author_last_name) < 100:
            paper_book.author_last_name = author_last_name
        else:
            raise ValueError('Last name of author should be a string and length between 1 and 100 symbols')

        self.session.add(paper_book)
        self.session.commit()
        return paper_book.id

    def change_paper_book(self, id_p_book, title, cover, length, width, weight, pages, isbn, author_first_name,
                          author_middle_name, author_last_name, release_year, category, language, annotation, publisher,
                          rating, pic) -> None:
        try:
            paper_book = self.session.query(PaperBook).get(id_p_book)
            if paper_book:
                if type(title) == str and 0 < len(title) < 200:
                    paper_book.book_title = title
                else:
                    raise ValueError('Title should be a string and length between 1 and 200 symbols')

                if cover in covers.keys():
                    paper_book.cover = cover
                else:
                    raise ValueError(f'Cover should be an integer and in {covers.keys()}')

                if type(length) == float and 0 <= length <= 300:
                    paper_book.length = length
                else:
                    raise ValueError('length of a paper book should be a float and between 0 and 300')

                if type(width) == float and 0 <= width <= 300:
                    paper_book.width = width
                else:
                    raise ValueError('width of a paper book should be a float and between 0 and 300')

                if type(weight) == float and 0 <= weight <= 10000:
                    paper_book.weight = weight
                else:
                    raise ValueError('weight of a paper book should be a float and between 0 and 10000')

                if type(pages) == int and 0 <= pages <= 23675:
                    paper_book.pages = pages
                else:
                    raise ValueError('pages of a paper book should be an int and between 0 and 23675')

                if len(isbn) == 13:
                    paper_book.isbn = isbn
                else:
                    raise ValueError('isbn of a paper book should be with 13 symbols long')

                if type(pic) == str and 0 < len(title) < 400:
                    paper_book.pic = pic
                else:
                    raise ValueError('Picture link should be a string and length between 1 and 400 symbols')

                if type(rating) == float and 0 <= rating <= 10:
                    paper_book.rating = rating
                else:
                    raise ValueError('rating of a ebook should be a float and between 0 and 10')

                if type(publisher) == str and 0 < len(title) < 200:
                    paper_book.publisher = publisher
                else:
                    raise ValueError('publisher should be a string and length between 1 and 200 symbols')

                if type(annotation) == str:
                    paper_book.annotation = annotation
                else:
                    raise ValueError('publisher should be a string')

                if len(language) != 2:
                    raise ValueError('Language should be set with 2 letters')
                if language in languages.keys():
                    paper_book.language = language
                else:
                    raise ValueError('Language should be set with 2 existing abbreviation letters')

                category_options = categories.keys()
                if category in category_options:
                    paper_book.category = category
                else:
                    raise ValueError(
                        f'category should be in between {min(category_options)} and {max(category_options)}')

                if release_year <= 1457:
                    raise ValueError('First printed book appeared in 1457 year')
                today_year = datetime.today().year
                if release_year > today_year:
                    raise ValueError(f'Year should be less than {today_year}')
                paper_book.release_year = release_year

                if type(author_first_name) == str and 0 < len(author_first_name) < 100:
                    paper_book.author_first_name = author_first_name
                else:
                    raise ValueError('First name of author should be a string and length between 1 and 100 symbols')

                if type(author_middle_name) == str and 0 < len(author_middle_name) < 100:
                    paper_book.author_middle_name = author_middle_name
                else:
                    raise ValueError('Middle name of author should be a string and length between 1 and 100 symbols')

                if type(author_last_name) == str and 0 < len(author_last_name) < 100:
                    paper_book.author_last_name = author_last_name
                else:
                    raise ValueError('Last name of author should be a string and length between 1 and 100 symbols')

                self.session.add(paper_book)
                self.session.commit()

            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print('The book was not changed', e)

    def rate_paper_book(self, id_p_book, rate):
        try:
            pb = self.session.query(PaperBook).get(id_p_book)
            if pb:
                if type(rate) == float and 0 <= rate <= 10:
                    pb.rating = rate
                else:
                    raise ValueError('rating of a paper book should be a float and between 0 and 10')
            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print('book was not rated: ', e)

    def remove_paper_book(self, id_p_book):
        try:
            pb = self.session.query(PaperBook).get(id_p_book)
            if pb:
                self.session.delete(pb)
                self.session.commit()
            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print('The book was not deleted', e)

    def get_paper_book_by_id(self, id_p_book):
        pb = self.session.query(PaperBook).get(id_p_book)
        if pb:
            return pb
        else:
            raise ValueError('Book with this ID does not exist in data base')

    def get_all_paper_book(self):
        """
        to get list of paper books
        :return: list of instances of PaperBook
        """
        pb_list = self.session.query(PaperBook).all()
        return pb_list

    def get_all_paper_book_newest_first(self):
        """
        to get list of paper books from newest to oldest
        :return: list of instances of PaperBook
        """
        pb_list = self.session.query(PaperBook).order_by(PaperBook._release_year.desc()).all()
        return pb_list

    def get_all_paper_book_oldest_first(self):
        """
        to get list of paper books from oldest to newest
        :return: list of instances of PaperBook
        """
        pb_list = self.session.query(PaperBook).order_by(PaperBook._release_year.asc()).all()
        return pb_list

    def get_paper_book_by_title(self, title):
        pb_list = self.session.query(PaperBook).filter(PaperBook._title.like(title)).all()
        return pb_list

    def get_paper_book_by_author_last_name(self, last_name):
        pb_list = self.session.query(PaperBook).filter(PaperBook._author_last_name.like(last_name)).all()
        return pb_list

    def get_paper_book_by_author_first_name(self, first_name):
        eb_list = self.session.query(PaperBook).filter(PaperBook._author_first_name.like(first_name)).all()
        return eb_list

    def get_paper_book_by_category(self, category):
        pb_list = self.session.query(PaperBook).filter(PaperBook._category == category).all()
        return pb_list

    def get_paper_book_by_release_year(self, year):
        pb_list = self.session.query(PaperBook).filter(PaperBook._release_year == year).all()
        return pb_list

    def get_paper_book_by_publisher(self, publisher):
        pb_list = self.session.query(PaperBook).filter(PaperBook._publisher.like(publisher)).all()
        return pb_list

    def get_paper_book_by_rating(self, min_rating=0, max_rating=10):
        pb_list = self.session.query(PaperBook).filter(PaperBook._rating <= max_rating,
                                                       PaperBook._rating >= min_rating).all()
        return pb_list
