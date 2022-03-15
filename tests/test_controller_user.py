from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from user import User
from wishlist import Wishlist
from controller_user import ControllerUser
from address import Address



C_F_NAME = "kurt"
C_L_NAME = "rogiers"
C_EMAIL =  "tevinden@vtm.altijd"
C_STATUS = 1

C_ADDRESS_STREET ="VTMstraat"
C_ADDRESS_NUMBER = "3"
C_ADDRESS_CITY ="Brussel"
C_ADDRESS_COUNTRY ="Belgie"
C_ADDRESS_POSTCODE ="4000"

C_ADDRESS_STREET_2="doesntmatter"
C_ADDRESS_NUMBER_2 = "NoIdea"
C_ADDRESS_CITY_2 ="stupidcity"
C_ADDRESS_COUNTRY_2 ="also doesnt matter"
C_ADDRESS_POSTCODE_2 ="az3 o3"

C_F_NAME_2= "Joe"
C_L_NAME_2="Biden"
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
        wishlist = Wishlist()
        wishlist.id =1

        adres2 = Address()
        adres2.id = 2
        adres2.street = C_ADDRESS_STREET_2
        adres2.number = C_ADDRESS_NUMBER_2
        adres2.postcode = C_ADDRESS_POSTCODE_2
        adres2.country = C_ADDRESS_COUNTRY_2


        wishlist2 = Wishlist()
        wishlist2.id = 2

        adres = Address()
        adres.id = 1
        adres.street =C_ADDRESS_STREET
        adres.number =C_ADDRESS_NUMBER
        adres.postcode=C_ADDRESS_POSTCODE
        adres.country = C_ADDRESS_COUNTRY
        adres.city=C_ADDRESS_CITY

        user2 = User()
        user2.address=adres2
        user2.wishlist=wishlist2

        user =User()
        user._email = C_EMAIL
        user._lastname = C_L_NAME
        user._firstname = C_F_NAME
        user.address=adres
        user.wishlist =wishlist
        self.controller =ControllerUser(self.session)
        self.session.add(user)
        self.session.add(adres)
        self.session.add(adres2)
        self.session.add(wishlist)
        self.session.add(wishlist2)
        self.session.commit()
        self.u= user
        self.a = adres
        self.a2 =adres2
        self.w2 =wishlist2
        self.w = wishlist
        self.u2 =user2



    def test_controller_get(self):
        id = self.u.id
        user = self.controller.get_user(id)
        self.assertEqual(user._firstname,C_F_NAME)
        self.assertEqual(user._lastname,C_L_NAME)
        self.assertEqual(user._email,C_EMAIL)
        self.assertEqual(user._status,C_STATUS)
        self.assertEqual(user.address.id,self.a.id)
        self.assertEqual(user.wishlist.id,self.w.id)

    def test_controller_add_user_happy_path(self):

        id2 = self.controller.add_user(C_F_NAME_2,C_L_NAME_2,C_EMAIL_2,self.a2,None,self.w2)
        user2= self.controller.get_user(id2)


        self.assertEqual(user2._firstname,C_F_NAME_2)
        self.assertEqual(user2._lastname,C_L_NAME_2)
        self.assertEqual(user2._email,C_EMAIL_2)
        self.assertEqual(user2._status,C_STATUS)
        self.assertEqual(user2.address.id,self.u2.address.id)
        self.assertEqual(user2.wishlist.id,self.u2.wishlist.id)

    def test_changes_controller(self):
        id = self.u.id
        self.controller.change_user(id,C_F_NAME_2,C_L_NAME_2,C_EMAIL_2,self.a2,None,self.w2)
        user = self.controller.get_user(id)

        self.assertEqual(user._firstname, C_F_NAME_2)
        self.assertEqual(user._lastname, C_L_NAME_2)
        self.assertEqual(user._email, C_EMAIL_2)
        self.assertEqual(user._status, C_STATUS)
        self.assertEqual(user.address.id, self.u2.address.id)
        self.assertEqual(user.wishlist.id, self.u2.wishlist.id)

    def test_get_all_users_ids(self):
        id = self.u.id
        id2 = self.controller.add_user(C_F_NAME_2, C_L_NAME_2, C_EMAIL_2, self.a2, None, self.w2)
        self.assertIn(id,self.controller.get_all_user_ids())
        self.assertIn(id2,self.controller.get_all_user_ids())
        self.assertNotIn(0,self.controller.get_all_user_ids())

    def test_does_id_excist(self):

        id = self.u.id
        id2 = self.controller.add_user(C_F_NAME_2, C_L_NAME_2, C_EMAIL_2, self.a2, None, self.w2)
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
        streets = list(map(lambda x: x.address._street,users))
        self.assertIn(C_ADDRESS_STREET,streets)

    def test_get_user_by_city(self):
        users = self.controller.get_user_by_city(C_ADDRESS_CITY)
        citys = list(map(lambda x: x.address._city,users))
        self.assertIn(C_ADDRESS_CITY,citys)

    def test_get_user_by_postcode(self):
        users = self.controller.get_user_by_postcode(C_ADDRESS_POSTCODE)
        postcodes = list(map(lambda x: x.address._postcode,users))
        self.assertIn(C_ADDRESS_POSTCODE,postcodes)


