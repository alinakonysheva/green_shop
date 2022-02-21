from datetime import datetime
from paper_book import PaperBook
from database import session
from constants import languages, categories, covers


# TODO change all numbers to constants
# TODO in errors add input

class ControllerPaperBook:

    @staticmethod
    def add_paper_book(title, cover, length, width, weight, pages, isbn, author_first_name, author_middle_name,
                       author_last_name, release_year, category, language, annotation, publisher, rating, pic):

        paper_book = PaperBook()

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

        if type(isbn) == int and len(str(isbn)) == 13:
            paper_book.isbn = isbn
        else:
            raise ValueError('isbn of a paper book should be an int and the number of digits == 13')

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

        session.add(paper_book)
        session.commit()

    @staticmethod
    def change_paper_book(id_p_book, title, cover, length, width, weight, pages, isbn, author_first_name,
                          author_middle_name, author_last_name, release_year, category, language, annotation, publisher,
                          rating, pic) -> None:
        try:
            paper_book = session.query(PaperBook).get(id_p_book)
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

                if type(isbn) == int and len(str(isbn)) == 13:
                    paper_book.isbn = isbn
                else:
                    raise ValueError('isbn of a paper book should be an int and the number of digits == 13')

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

                session.add(paper_book)
                session.commit()

            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print('The book was not changed', e)

    @staticmethod
    def rate_paper_book(id_p_book, rate):
        try:
            pb = session.query(PaperBook).get(id_p_book)
            if pb:
                if type(rate) == float and 0 <= rate <= 10:
                    pb.rating = rate
                else:
                    raise ValueError('rating of a paper book should be a float and between 0 and 10')
            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print('book was not rated: ', e)

    @staticmethod
    def remove_paper_book(id_p_book):
        try:
            pb = session.query(PaperBook).get(id_p_book)
            if pb:
                session.delete(pb)
                session.commit()
            else:
                raise ValueError('Book with this ID does not exist in data base')
        except Exception as e:
            print('The book was not deleted', e)

    @staticmethod
    def get_paper_book_by_id(id_p_book):
        pb = session.query(PaperBook).get(id_p_book)
        return pb

    @staticmethod
    def get_all_paper_book():
        """
        to get list of paper books
        :return: list of instances of PaperBook
        """
        pb_list = session.query(PaperBook).all()
        return pb_list

    @staticmethod
    def get_all_paper_book_newest_first():
        """
        to get list of paper books from newest to oldest
        :return: list of instances of PaperBook
        """
        pb_list = session.query(PaperBook).order_by(PaperBook.release_year.desc()).all()
        return pb_list

    @staticmethod
    def get_all_paper_book_oldest_first():
        """
        to get list of paper books from oldest to newest
        :return: list of instances of PaperBook
        """
        pb_list = session.query(PaperBook).order_by(PaperBook.release_year.asc()).all()
        return pb_list

    @staticmethod
    def get_paper_book_by_title(title):
        pb_list = session.query(PaperBook).filter(PaperBook.book_title.like(title)).all()
        return pb_list

    @staticmethod
    def get_paper_book_by_author_last_name(last_name):
        pb_list = session.query(PaperBook).filter(PaperBook.author_last_name.like(last_name)).all()
        return pb_list

    @staticmethod
    def get_paper_book_by_author_first_name(first_name):
        eb_list = session.query(PaperBook).filter(PaperBook.author_first_name.like(first_name)).all()
        return eb_list

    # TODO: not sure if it will be working with usual property
    @staticmethod
    def get_paper_book_by_author_full_name(full_name):
        pb_list = session.query(PaperBook).filter(PaperBook.author_full_name.like(full_name)).all()
        return pb_list

    @staticmethod
    def get_paper_book_by_category(category):
        pb_list = session.query(PaperBook).filter(PaperBook.category == category).all()
        return pb_list

    @staticmethod
    def get_paper_book_by_author_last_name(last_name):
        pb_list = session.query(PaperBook).filter(PaperBook.author_last_name.like(last_name)).all()
        return pb_list

    @staticmethod
    def get_paper_book_by_release_year(year):
        pb_list = session.query(PaperBook).filter(PaperBook.release_year == year).all()
        return pb_list

    @staticmethod
    def get_paper_book_by_publisher(publisher):
        pb_list = session.query(PaperBook).filter(PaperBook.publisher.like(publisher)).all()
        return pb_list

    @staticmethod
    def get_paper_book_by_rating(min_rating=0, max_rating=10):
        pb_list = session.query(PaperBook).filter(PaperBook.rating <= max_rating, PaperBook.rating >= min_rating).all()
        return pb_list
