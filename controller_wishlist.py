from wishlist import Wishlist


class ControllerWishlist:
    def __init__(self, session):
        self.session = session

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
