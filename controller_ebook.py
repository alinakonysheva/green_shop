from datetime import datetime
from e_book import EBook
from database import session
from constants import languages, categories


class ControllerBook:
    @staticmethod
    def add_ebook(title, size, author_first_name, author_middle_name, author_last_name, release_year,
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

        session.add(ebook)
        session.commit()

    @staticmethod
    def change_wishlist(id_wishlist, id_user) -> None:
        """
        to update user's id in the wishlist
        :param id_wishlist
        :param id_user
        """
        wl = session.query(Wishlist).get(id_wishlist)
        wl.id_user = id_user

        session.add(wl)
        session.commit()

    @staticmethod
    def remove_wishlist(id_wishlist):
        wl = session.query(Wishlist).get(id_wishlist)
        session.delete(wl)
        session.commit()

    @staticmethod
    def get_wishlist(id_wishlist):
        """
        to get wishlist by wishlist's id
        :param id_wishlist:
        :return:
        """
        wl = session.query(Wishlist).get(id_wishlist)
        return wl

    @staticmethod
    def get_wishlist_by_user(id_user):
        """
        to get a wishlist by user id
        :param id_user
        :return: instance of  Wishlist by id_user
        """
        wl = session.query(Wishlist).filter(Wishlist.id_user == id_user).all()[0]
        return wl

    @staticmethod
    def is_wishlist_by_user(id_user) -> object:
        wl = session.query(Wishlist).filter(Wishlist.id_user == id_user).all()[0]
        if wl:
            return True
        else:
            return False

    @staticmethod
    def add_ebook_in_wishlist_by_id_wishlist(id_wishlist):
        pass

    @staticmethod
    def add_ebook_in_wishlist_by_id_user(id_user):
        pass
