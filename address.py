from sqlalchemy.ext.hybrid import hybrid_property
from database import BaseObj
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from user import User


class Address(BaseObj):
    __tablename__ = "T_ADDRESS"
    _street = Column('STREET', String(88))
    _number = Column('NUMBER', String(10))
    _city = Column('CITY', String(200))
    _country = Column('C0UNTRY', String(30))
    _postcode = Column('POSTCODE', String(30))
    user_id = Column('F_USER_ID', ForeignKey(User.id), index=True)
    user = relationship(User, foreign_keys='Address.user_id', back_populates="address")

    @hybrid_property
    def street(self):
        return self._street.capitalize()

    @street.setter
    def street(self, value):
        self._street = value

    @hybrid_property
    def number(self):
        return self._number.capitalize()

    @number.setter
    def number(self, value):
        v = value.strip()
        special_characters = '!@ # $%^&*()-+?_=,<">'
        for char in v:
            if char in special_characters:
                raise ValueError('a number cannot contain special characters')
        self._number = value

    @hybrid_property
    def city(self):
        return self._city.capitalize()

    @city.setter
    def city(self, value):
        self._city = value

    @hybrid_property
    def country(self):
        return self._country.capitalize()

    @country.setter
    def country(self, value):
        v = value.strip()
        special_characters = '!@#$%^&*()-+?_=,<">/'
        for char in v:
            if char in special_characters:
                raise ValueError('a country cannot contain special characters')
        self._country = value

    @hybrid_property
    def postcode(self):
        return self._postcode

    @postcode.setter
    def postcode(self, value):
        v = value.strip()
        if len(v) <= 30:
            self._postcode = value
        else:
            raise ValueError('postcode can not be longer than 30 symbols')
