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

C_STREET_2 = 'Street Baker'
C_NUMBER_2 = '121A'
C_CITY_2 ='Manchester'
C_COUNTRY_2 = 'The United Kingdom of Great Britain and Northern Ireland'
C_POSTCODE_2 = 'SE2 9YW'

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
        address.user = user_1
        self.session.add(address)
        self.session.add(user_1)
        self.session.commit()

        self.controller = ControllerAddress(self.session)
        self.address = address
        self.user = user_1

    def test_controller_get(self):
        id = self.address.id
        address = self.controller.get_address(id)
        self.assertEqual(address.city,C_CITY)
        self.assertEqual(address.street,C_STREET)
        self.assertEqual(address.number,C_NUMBER)
        self.assertEqual(address.postcode,C_POSTCODE)
        self.assertEqual(address.country,C_COUNTRY)

    def test_controller_change_address(self):
        id = self.address.id
        self.controller.change_address(id,C_STREET_2,C_NUMBER_2,C_POSTCODE_2,C_CITY_2,C_COUNTRY_2)
        address2 = self.controller.get_address(id)

        self.assertEqual(address2.city, C_CITY_2)
        self.assertEqual(address2.street, C_STREET_2)
        self.assertEqual(address2.number, C_NUMBER_2)
        self.assertEqual(address2.postcode, C_POSTCODE_2)
        self.assertEqual(address2.country, C_COUNTRY_2)
    def test_controller_add_address_happy_path(self):
        id2 =self.controller.add_address(C_STREET_2,C_NUMBER_2,C_POSTCODE_2,C_CITY_2,C_COUNTRY_2)
        address2 = self.controller.get_address(id2)

        self.assertEqual(address2.city, C_CITY_2)
        self.assertEqual(address2.street, C_STREET_2)
        self.assertEqual(address2.number, C_NUMBER_2)
        self.assertEqual(address2.postcode, C_POSTCODE_2)
        self.assertEqual(address2.country, C_COUNTRY_2)

    def test_get_address_by_street(self):
        addresses = self.controller.get_address_by_street(C_STREET)
        streets = list(map(lambda x: x._street, addresses))
        self.assertIn(C_STREET, streets)

    def test_get_address_by_city(self):
        addresses = self.controller.get_address_by_city(C_CITY)
        citys = list(map(lambda x: x._city, addresses))
        self.assertIn(C_CITY, citys)

    def test_get_address_by_postcode(self):
        addresses = self.controller.get_address_by_postcode(C_POSTCODE)
        postcodes = list(map(lambda x: x._postcode, addresses))
        self.assertIn(C_POSTCODE, postcodes)

    def test_get_address_by_user_firstname(self):
        addresses = self.controller.get_address_by_user_firstname(C_FIRST_NAME)
        names = list(map(lambda x: x.User._firstname, addresses))
        self.assertIn(C_FIRST_NAME, names)

    def test_get_address_by_user_lastname(self):
        addresses = self.controller.get_address_by_user_lastname(C_LAST_NAME)
        names = list(map(lambda x: x.User._lastname, addresses))
        self.assertIn(C_LAST_NAME, names)
