from datetime import datetime
from audio_book import AudioBook
from database import session
from constants import languages, categories


class ControllerAudioBook:

    @staticmethod
    def add_audiobook(title, reader_first_name, reader_last_name, reader_middle_name, duration_hours, duration_minutes,
                       duration_seconds, author_first_name, author_middle_name, author_last_name, release_year,
                       category, language, annotation, publisher, rating, pic):

        audiobook = AudioBook()

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

        session.add(audiobook)
        session.commit()

    @staticmethod
    def change_audiobook(id_audiobook, title, reader_first_name, reader_last_name, reader_middle_name, duration_hours,
                         duration_minutes,
                         duration_seconds, author_first_name, author_middle_name, author_last_name, release_year,
                         category, language, annotation, publisher, rating, pic):
        try:
            audiobook = session.query(AudioBook).get(id_audiobook)
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

                session.add(audiobook)
                session.commit()
            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print(e)

    @staticmethod
    def rate_audiobook(id_audiobook, rate):
        try:
            ab = session.query(AudioBook).get(id_audiobook)
            if ab:
                if type(rate) == float and 0 <= rate <= 10:
                    ab.rating = rate
                else:
                    raise ValueError('rating of a ebook should be a float and between 0 and 10')
            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print('book was not rated: ', e)

    @staticmethod
    def remove_audiobook(id_audiobook):
        try:
            ab = session.query(AudioBook).get(id_audiobook)
            session.delete(ab)
            session.commit()
        except Exception as e:
            print(e, 'this book does not exist')

    @staticmethod
    def get_audiobook_by_id(id_audiobook):
        ab = session.query(AudioBook).get(id_audiobook)
        return ab

    @staticmethod
    def get_all_audiobook():
        """
        to get list of audio_book
        :return: list of instances of Audiobook
        """
        ab_list = session.query(AudioBook).all()
        return ab_list

    @staticmethod
    def get_all_audiobook_newest_first():
        """
        to get list of audio_book from newest to oldest
        :return: list of instances of AudioBook
        """
        ab_list = session.query(AudioBook).order_by(AudioBook.release_year.desc()).all()
        return ab_list

    @staticmethod
    def get_all_audiobook_oldest_first():
        """
        to get list of audio_books from oldest to newest
        :return: list of instances of AudioBook
        """
        ab_list = session.query(AudioBook).order_by(AudioBook.release_year.asc()).all()
        return ab_list

    @staticmethod
    def get_audiobook_by_title(title):
        ab_list = session.query(AudioBook).filter(AudioBook.book_title.like(title)).all()
        return ab_list

    @staticmethod
    def get_audiobook_by_author_last_name(last_name):
        ab_list = session.query(AudioBook).filter(AudioBook.author_last_name.like(last_name)).all()
        return ab_list

    @staticmethod
    def get_audiobook_by_author_first_name(first_name):
        eb_list = session.query(AudioBook).filter(AudioBook.author_first_name.like(first_name)).all()
        return eb_list

    # TODO: not sure if it will be working with usual property
    @staticmethod
    def get_audiobook_by_author_full_name(full_name):
        ab_list = session.query(AudioBook).filter(AudioBook.author_full_name.like(full_name)).all()
        return ab_list

    @staticmethod
    def get_audiobook_by_category(category):
        ab_list = session.query(AudioBook).filter(AudioBook.category == category).all()
        return ab_list

    @staticmethod
    def get_audiobook_by_author_last_name(last_name):
        ab_list = session.query(AudioBook).filter(AudioBook.author_last_name.like(last_name)).all()
        return ab_list

    @staticmethod
    def get_audiobook_by_release_year(year):
        ab_list = session.query(AudioBook).filter(AudioBook.release_year == year).all()
        return ab_list

    @staticmethod
    def get_audiobook_by_publisher(publisher):
        ab_list = session.query(AudioBook).filter(AudioBook.publisher.like(publisher)).all()
        return ab_list

    @staticmethod
    def get_audiobook_by_rating(min_rating=0, max_rating=10):
        ab_list = session.query(AudioBook).filter(AudioBook.rating <= max_rating, AudioBook.rating >= min_rating).all()
        return ab_list
