from wishlist import Wishlist
from wishlistbook import WishlistBook
from controller_book import ControllerBook


class ControllerWishlist:
    def __init__(self, session):
        self.session = session
        self.controller_book = ControllerBook(session)

    def add_wishlist(self, id_user):
        # TODO: IF id_user exists, else raise exception
        wl = Wishlist()
        wl.id_user = id_user

        self.session.add(wl)
        self.session.commit()
        return wl.id

    def change_user_in_wishlist(self, id_wishlist, id_user) -> None:
        """
        to update user's id in the wishlist
        :param id_wishlist
        :param id_user
        """
        try:
            wl = self.session.query(Wishlist).get(id_wishlist)
            if wl:
                wl.id_user = id_user
                self.session.add(wl)
                self.session.commit()
            else:
                raise ValueError(f'Wishlist with #{id_wishlist} does nor exist in database')
        except Exception as e:
            print(e)

    def remove_wishlist(self, id_wishlist):
        try:
            wl = self.session.query(Wishlist).get(id_wishlist)
            if wl:
                self.session.delete(wl)
                self.session.commit()
            else:
                raise ValueError(f'Wishlist with #{id_wishlist} does not exist in database')
        except Exception as e:
            print(e)

    def get_wishlist_by_id(self, id_wishlist):
        """
        to get wishlist by wishlist's id
        :param id_wishlist:
        :return:
        """
        wl = self.session.query(Wishlist).get(id_wishlist)
        if wl:
            return wl
        else:
            raise ValueError(f'Wishlist with #{id_wishlist} does not exist in database')

    def get_wishlist_by_user(self, id_user):
        """
        to get a wishlist by user id
        :param id_user
        :return: instance of  Wishlist by id_user
        """
        # TODO: if id_user exists!!!

        wl = self.session.query(Wishlist).filter(Wishlist.id_user == id_user).all()[0]
        return wl

    def is_wishlist_by_user(self, id_user) -> object:
        # TODO: if id_user exists!!!
        wl = self.session.query(Wishlist).filter(Wishlist.id_user == id_user).all()[0]
        if wl:
            return True
        else:
            return False

    # get all existing ids
    def get_all_wishlists_ids(self):
        """
        to get list of all existing id's
        :return: list of str(id)
        """
        id_list = list(map(lambda x: x.id, self.session.query(Wishlist).all()))
        return id_list

    ####################################################
    def add_book_to_wishlist(self, id_wishlist, id_book):
        wishlist_book = WishlistBook()

        if id_wishlist in self.get_all_wishlists_ids():
            wishlist_book.id_wishlist = id_wishlist
            if id_book in self.controller_book.get_all_ids():
                wishlist_book.id_book = id_book
                self.session.add(wishlist_book)
                self.session.commit()
            else:
                raise ValueError('Book with this ID does not exist in data base')
        else:
            raise ValueError('Wishlist with this ID does not exist in data base')

    def delete_book_from_wishlist(self, id_wishlist_to_book):

        book_to_wishlist = self.session.query(WishlistBook).get(id_wishlist_to_book)
        if book_to_wishlist:
            self.session.delete(book_to_wishlist)
            self.session.commit()
        else:
            raise ValueError(f'Relation with this ID {id_wishlist_to_book} does not exist in data base')

    def get_all_book_ids_by_wishlist(self, id_wishlist):
        if id_wishlist in self.get_all_wishlists_ids():
            books = self.session.query(WishlistBook).filter(WishlistBook.id_wishlist == id_wishlist).all()
            books_ids = list(map(lambda x: x.id, books))
            return books_ids
        else:
            raise ValueError('Wishlist with this ID does not exist in data base')
