from sqlalchemy.ext.hybrid import hybrid_property
from database import BaseObj
from sqlalchemy import Column, String, Integer, Float, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from address import Address


class User(BaseObj):
    __tablename__ = "T_USER"
    id = Column('USER_ID', Integer, primary_key=True)
    _firstname = Column('FIRST_NAME', String())
    _lastname = Column('LAST_NAME', String())
    _email = Column('EMAIL', String())
    password = Column('PASSWORD', String())
    status = Column('STATUS', Integer, default=0)
    wishlist = Column('WISHLIST', Integer)
    address_id = Column('ADDRESS_ID', ForeignKey(Address.addressid), index=True)
    address = relationship(Address, Foreign_keys='User.addresid', back_populates="user")


    @hybrid_property
    def firstname(self):
        return str(self._firstname).capitalize()

    @firstname.setter
    def firstname(self, value):
        v = value.strip()
        special_characters = '!@ # $%^&*()-+?_=,<">/'
        for char in v:
            if v in special_characters:
                raise valueError('a name cannot contain special characters')
        self._firstname = value

    @hybrid_property
    def lastname(self):
        return str(self._lastname).capitalize()

    @lastname.setter
    def lastname(self, value):
        v = value.strip()
        special_characters = '!@ # $%^&*()-+?_=,<">/'
        for char in v:
            if v in special_characters:
                raise valueError('a name cannot contain special characters')
        self._lastname = value

    @hybrid_property
    def email(self):
        return str(self._email).capitalize()

    @email.setter
    def email(self, value):
        v = value.strip()
        valid = False
        for char in v:
            if v == '@':
                valid = True
        if valid == True:
            self._email = value
        else:
            raise valueError('no valid email')

    @hybrid_property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value == 0 or value == 1:
            self._status = value
        else:
            raise valueError('no valid admin status')

    @property
    def __str__(self) -> str:
        return f'{self._firstname} {self._lastname}'
