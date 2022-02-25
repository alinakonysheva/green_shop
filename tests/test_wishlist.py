from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from wishlist import Wishlist
from user import User
from controller_wishlist import ControllerWishlist
from e_book import EBook


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


