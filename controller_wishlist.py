from wishlist import Wishlist
from database import session


class ControllerWishlist:
    @staticmethod
    def add_wishlist(id_user):
        wl = Wishlist()
        wl.id_user = id_user

        session.add(wl)
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
