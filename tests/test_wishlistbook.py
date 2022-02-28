from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from wishlist import Wishlist
from user import User
from wishlistbook import WishlistBook
from e_book import EBook

C_TITLE = 'Staring at the Sun'


class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')

    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class WishlistBookTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_wishlist_book(self):
        ebook = EBook()
        ebook.book_title = C_TITLE
        self.session.add(ebook)
        self.session.commit()
        user_1 = User()
        self.session.add(user_1)
        self.session.commit()
        wishlist = Wishlist()
        wishlist.id_user = user_1.id
        self.session.add(wishlist)
        self.session.commit()
        wishlist_book = WishlistBook()
        wishlist_book.id_book = ebook.id
        wishlist_book.id_wishlist = wishlist.id
        self.session.add(wishlist_book)
        self.session.commit()

        wlb_from_query = self.session.query(WishlistBook).get(1)
        self.assertEqual(wlb_from_query.id_wishlist, wishlist_book.id_wishlist)
        self.assertEqual(wlb_from_query.id_book, wishlist_book.id_book)
