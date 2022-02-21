from book import Book
from database import session


class ControllerBook:
    # get all existing ids
    @staticmethod
    def get_all_ids():
        """
        to get list of all existing id's
        :return: list of str(id)
        """
        id_list = list(map(lambda x: x.id, session.query(Book).all()))
        return id_list
