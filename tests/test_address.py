from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from address import Address

C_STREET = 'Baker Street'
C_NUMBER = '221B'
C_CITY = 'London'
C_COUNTRY = 'Great Britain'
C_POSTCODE = 'NW1 6XE'


class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class AddressTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_address_happy_path(self):
        address = Address()
        address.street = C_STREET
        address.number = C_NUMBER
        address.city = C_CITY
        address.country = C_COUNTRY
        address.postcode = C_POSTCODE

        self.session.add(address)
        self.session.commit()

        address_from_query = self.session.query(Address).get(1)
        self.assertEqual(address_from_query.street, C_STREET.capitalize())
        self.assertEqual(address_from_query.number, C_NUMBER.capitalize())
        self.assertEqual(address_from_query.city, C_CITY.capitalize())
        self.assertEqual(address_from_query.country, C_COUNTRY.capitalize())
        self.assertEqual(address_from_query.postcode, C_POSTCODE)
