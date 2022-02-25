from book import Book


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
