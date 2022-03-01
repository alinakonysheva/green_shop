from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from user import User

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
#TODO: add reletionship with wishlist
#TODO: check relationship with address


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

        self.session.add(user)
        self.session.commit()

        user_from_query = self.session.query(User).get(1)
        self.assertEqual(user_from_query.firstname, C_FIRST_NAME)
        self.assertEqual(user_from_query.lastname, C_LAST_NAME)
        self.assertEqual(user_from_query.email, C_EMAIL)
        self.assertEqual(user_from_query.status, C_STATUS)
