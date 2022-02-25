from datetime import datetime
from e_book import EBook
from constants import languages, categories


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
