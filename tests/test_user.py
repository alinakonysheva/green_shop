from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from user import User
from wishlist import Wishlist
from address import Address

C_LAST_NAME = 'Yalom'
C_LAST_NAME_2 = 'Yalom2'
C_INCORRECT_LAST_NAME_LONG = str('[i for i in ...]')
C_INCORRECT_LAST_NAME_SHORT = ''
C_FIRST_NAME = 'Irvin'
C_FIRST_NAME_2 = 'Irvin2'
C_INCORRECT_FIRST_NAME_LONG = str('[i for i in ...]')
C_INCORRECT_FIRST_NAME_SHORT = ''
C_EMAIL = 'irvinYalom@gmail.com'
C_STATUS = 1

C_TITLE = 'Staring at the Sun'

C_STREET = 'Baker Street'
C_NUMBER = '221B'
C_CITY = 'London'
C_COUNTRY = 'Great Britain'
C_POSTCODE = 'NW1 6XE'

C_TITLE = 'Staring at the Sun'
C_AUTHOR_LAST_NAME = 'Yalom'
C_AUTHOR_FIRST_NAME = 'Irvin'
C_AUTHOR_MIDDLE_NAME = 'David'
C_RELEASE_YEAR = 2008
C_RATING = 9.9
C_PIC = '/dsfgasdfgad'
C_CATEGORY = 3
C_LANGUAGE = "nl"
C_ANNOTATION = "Written in Irv Yalom's inimitable story-telling style, Staring at the Sun is a profoundly encouraging" \
               "approach to the universal issue of mortality. In this magisterial opus, capping a lifetime of work and" \
               "personal experience, Dr. Yalom helps us recognize that the fear of death is at the heart of much of " \
               "our anxiety. Such recognition is often catalyzed by an \"awakening experience\"—a dream, \" \
               \"or loss (the death of a loved one, divorce, loss of a job or home), illness, trauma, or aging."
C_PUBLISHER = "Wiley"
C_SIZE = 56.0


class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class UserTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_user_happy_path(self):
        user = User()
        user.firstname = C_FIRST_NAME
        user.lastname = C_LAST_NAME
        user.email = C_EMAIL
        user.status = C_STATUS

        address = Address()
        address.street = C_STREET
        address.number = C_NUMBER
        address.city = C_CITY
        address.country = C_COUNTRY
        address.postcode = C_POSTCODE
        user.address = [address]
        self.session.add(address)
        self.session.commit()
        wishlist = Wishlist()
        wishlist.id_user = user.id
        self.session.add(wishlist)
        self.session.commit()

        user.wishlist = [wishlist]
        self.session.add(user)
        self.session.commit()

        user_from_query = self.session.query(User).get(1)
        self.assertEqual(user_from_query.firstname, C_FIRST_NAME)
        self.assertEqual(user_from_query.lastname, C_LAST_NAME)
        self.assertEqual(user_from_query.email, C_EMAIL)
        self.assertEqual(user_from_query.status, C_STATUS)
        wishlist_from_user_from_query = user_from_query.wishlist[0]
        self.assertEqual(wishlist_from_user_from_query.id_user, user.id)
        address_from_user_from_query = user_from_query.address[0]
        self.assertEqual(address_from_user_from_query.street, C_STREET.capitalize())
        self.assertEqual(address_from_user_from_query.number, C_NUMBER.capitalize())
        self.assertEqual(address_from_user_from_query.city, C_CITY.capitalize())
        self.assertEqual(address_from_user_from_query.country, C_COUNTRY.capitalize())
        self.assertEqual(address_from_user_from_query.postcode, C_POSTCODE)
