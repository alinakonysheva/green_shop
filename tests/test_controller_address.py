from abc import abstractmethod
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
