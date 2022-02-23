from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from wishlist import Wishlist
from user import User
from controller_wishlist import ControllerWishlist


class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class WishlistTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_wishlist(self):
        user_1 = User()
        wishlist = Wishlist()
        wishlist.id_user = user_1.id
        self.session.add(wishlist)
        self.session.commit()

        wl_from_query = self.session.query(Wishlist).get(1)
        self.assertEqual(wl_from_query.id_user, wishlist.id_user)


class ControllerWishlistTests(BaseDbTest):
    def do_setup(self):
        wishlist = Wishlist()
        user_1 = User()
        wishlist.id_user = user_1.id

        self.controller = ControllerWishlist(self.session)
        self.session.add(wishlist)
        self.session.commit()
        self.wishlist = wishlist
        self.user = user_1

    def test_get_wishlist(self):
        id_wishlist = self.wishlist.id
        wl = self.controller.get_wishlist_by_id(id_wishlist)
        self.assertEqual(wl.id_user, self.user.id)

    def test_change_user_in_wishlist(self):
        user_2 = User()
        id_user_2 = user_2.id
        self.controller.change_user_in_wishlist(self.wishlist.id, id_user_2)
        wl = self.controller.get_wishlist_by_id(self.wishlist.id)
        self.assertEqual(id_user_2, wl.id_user)

    def test_add_wishlist(self):
        user_3 = User()
        id_user_3 = user_3.id
        id_new_wishlist = self.controller.add_wishlist(id_user_3)
        wl = self.controller.get_wishlist_by_id(id_new_wishlist)
        self.assertEqual(wl.id_user, id_user_3)

    def test_remove_wishlist(self):
        # TODO: with real users
        # user_3 = User()
        # id_user_3 = user_3.id
        id_user_3 = 3
        id_new_wishlist = self.controller.add_wishlist(id_user_3)
        self.controller.remove_wishlist(id_new_wishlist)
        with self.assertRaises(ValueError):
            self.controller.get_wishlist_by_id(id_new_wishlist)

    def test_get_wishlist_by_user(self):
        wl = self.controller.get_wishlist_by_user(self.user.id)
        self.assertEqual(wl.id, self.wishlist.id)

    def test_is_wishlist_by_user(self):
        self.assertTrue(self.controller.get_wishlist_by_user(self.user.id))

    def test_get_all_wishlists_ids(self):
        list_with_wl_ids = self.controller.get_all_wishlists_ids()
        self.assertTrue(type(list_with_wl_ids) == list)
        self.assertIn(self.wishlist.id, list_with_wl_ids)

        user5 = User()
        wl_id = self.controller.add_wishlist(user5.id)
        list_with_wl_ids_2 = self.controller.get_all_wishlists_ids()
        self.assertIn(wl_id, list_with_wl_ids_2)
