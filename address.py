from sqlalchemy.ext.hybrid import hybrid_property
from database import BaseObj
from sqlalchemy import Column, String, Integer, Float, Text, Boolean
from sqlalchemy.orm import relationship


class Address(BaseObj):
    __tablename__ = "T_ADDRESS"
    _street = Column('STREET', String(88))
    _number = Column('NUMBER', String(10))
    _city = Column('CITY', String(200))
    _country = Column('C0UNTRY', String(30))
    _postcode = Column('POSTCODE', Integer)
    user = relationship('User', back_populates="address")

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
        special_characters = '!@ # $%^&*()-+?_=,<">/'
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
        special_characters = '!@ # $%^&*()-+?_=,<">/'
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
        for i in v:
            if i is not int:
                raise ValueError('a postcode only contains numbers')
        self._postcode = value
