"""from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from address import Address
from user import User
from controller_address import ControllerAddress

C_STREET = 'Baker Street'
C_NUMBER = '221B'
C_CITY = 'London'
C_COUNTRY = 'Great Britain'
C_POSTCODE = 'NW1 6XE'

C_LAST_NAME = 'Yalom'
C_LAST_NAME_2 = 'Yalom2'
C_FIRST_NAME = 'Irvin'
C_FIRST_NAME_2 = 'Irvin2'
C_EMAIL = 'irvinYalom@gmail.com'
C_EMAIL_2 = 'irvYalom@gmail.com'
C_STATUS = 1
C_STATUS_2 = 0

class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class ControllerAddressTests(BaseDbTest):
    def do_setup(self):
        address = Address()
        address.street = C_STREET
        address.number = C_NUMBER
        address.city = C_CITY
        address.country = C_COUNTRY
        address.postcode = C_POSTCODE
        user_1 = User()
        user_1.firstname = C_FIRST_NAME
        user_1.lastname = C_LAST_NAME
        user_1.email = C_EMAIL
        user_1.status = C_STATUS
        address.user_id = user_1.id
        self.session.add(address)
        self.session.add(address)
        self.session.commit(user_1)

        self.controller = ControllerAddress(self.session)
        self.address = address
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

    def test_add_book_to_wishlist_get_all_book_ids_by_wishlist(self):
        self.controller.add_book_to_wishlist(self.wishlist.id, self.book.id)
        id_books = self.controller.get_all_book_ids_by_wishlist(self.wishlist.id)
        self.assertTrue(type(id_books) == list)
        self.assertIn(self.book.id, id_books)
"""