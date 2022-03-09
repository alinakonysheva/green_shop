from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from user import User
from controller_user import ControllerUser
from address import Address


C_F_NAME = "Vladimir"
C_L_NAME = "Poetin"
C_EMAIL =  "Ukraïn@russia.now"
C_STATUS = 1
C_ADDRESS = 1
C_WISHLIST =1
C_USER_ID =1

C_ADDRESS_STREET ="Tiranstreet"
C_ADDRESS_NUMBER = "65b"
C_ADDRESS_CITY ="Moskou"
C_ADDRESS_COUNTRY ="The great Russia"
C_ADDRESS_POSTCODE ="2020"

C_F_NAME_2= "Joe"
C_L_NAME_2="Biden"
C_ADDRESS_2 =2
C_WISHLIST_2 =2
C_EMAIL_2 = "living@whitehouse.lit"
C_STATUS=1



class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

        @abstractmethod
        def do_setup(self):
            pass

class UserControllerTest(BaseDbTest):
    def do_setup(self):
        user =User()
        user._email = C_EMAIL
        user._lastname = C_L_NAME
        user._firstname = C_F_NAME
        user.address=C_ADDRESS
        self.controller =ControllerUser(self.session)
        self.session.add(user)
        self.session.commit()
        self.u= user

        address =Address()
        address.id=1

    def test_controller_get(self):
        id = self.u.id
        user = self.controller.get_user(id)
        self.assertEqual(user._firstname,C_F_NAME)
        self.assertEqual(user._lastname,C_L_NAME)
        self.assertEqual(user._email,C_EMAIL)
        self.assertEqual(user._status,C_STATUS)
        #self.assertEqual(user.address,C_ADDRESS)
        #self.assertEqual(user.wishlist,C_WISHLIST)

    def test_controller_add_user_happy_path(self):
        id2 = self.controller.add_user(C_F_NAME_2,C_L_NAME_2,C_EMAIL_2,C_ADDRESS_2,None,C_WISHLIST_2)
        user2= self.controller.get_user(id2)

        self.assertEqual(user2._firstname,C_F_NAME_2)
        self.assertEqual(user2._lastname,C_L_NAME_2)
        self.assertEqual(user2._email,C_EMAIL_2)
        self.assertEqual(user2._status,C_STATUS)
        self.assertEqual(user2.address,C_ADDRESS_2)
        self.assertEqual(user2.wishlist,C_WISHLIST_2)

    def test_changes_controller(self):
        id = self.u.id
        self.controller.change_user(id,C_F_NAME_2,C_L_NAME_2,C_EMAIL_2,C_ADDRESS_2,None,C_WISHLIST_2)

        user2 = self.controller.get_user(id)

        self.assertEqual(user2._firstname, C_F_NAME_2)
        self.assertEqual(user2._lastname, C_L_NAME_2)
        self.assertEqual(user2._email, C_EMAIL_2)
        self.assertEqual(user2._status, C_STATUS)
        self.assertEqual(user2.address, C_ADDRESS_2)
        self.assertEqual(user2.wishlist, C_WISHLIST_2)

    def test_get_all_users_ids(self):
        id = self.u.id
        id2 = self.controller.add_user(C_F_NAME_2, C_L_NAME_2, C_EMAIL_2, C_ADDRESS_2, None, C_WISHLIST_2)
        self.assertIn(id,self.controller.get_all_user_ids())
        self.assertIn(id2,self.controller.get_all_user_ids())
        self.assertNotIn(0,self.controller.get_all_user_ids())

    def test_does_id_excist(self):
        id = self.u.id
        id2 = self.controller.add_user(C_F_NAME_2, C_L_NAME_2, C_EMAIL_2, C_ADDRESS_2, None, C_WISHLIST_2)
        self.assertTrue(self.controller.does_user_excist(id))
        self.assertTrue(self.controller.does_user_excist(id2))
        self.assertFalse(self.controller.does_user_excist(0))

    def test_get_user_by_firstname(self):
        users = self.controller.get_user_by_firstname(C_F_NAME)
        firstnames = list(map(lambda x: x._firstname,users))
        self.assertIn(C_F_NAME,firstnames)

    def test_get_user_by_lastname(self):
        users = self.controller.get_user_by_lastname(C_L_NAME)
        names = list(map(lambda x: x._lastname,users))
        self.assertIn(C_L_NAME,names)

    def test_get_user_by_email(self):
        users = self.controller.get_user_by_email(C_EMAIL)
        emails = list(map(lambda x: x._email,users))
        self.assertIn(C_EMAIL,emails)

    def test_get_user_by_street(self):
        users = self.controller.get_user_by_street(C_ADDRESS_STREET)
        streets = list(map(lambda x: x.Address._street,users))
        self.assertIn(C_ADDRESS_STREET,streets)

    def test_get_user_by_city(self):
        users = self.controller.get_user_by_city(C_ADDRESS_CITY)
        citys = list(map(lambda x: x.Address._city,users))
        self.assertIn(C_ADDRESS_CITY,citys)

    def test_get_user_by_postcode(self):
        users = self.controller.get_user_by_postcode(C_ADDRESS_POSTCODE)
        postcodes = list(map(lambda x: x.Address._postcode,users))
        self.assertIn(C_ADDRESS_POSTCODE,postcodes)


