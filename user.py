from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from database import BaseObj
from sqlalchemy import Column, String, Integer
from constants import status_role


class User(BaseObj):
    __tablename__ = "T_USER"

    _firstname = Column('FIRST_NAME', String(50))
    _lastname = Column('LAST_NAME', String(50))
    _email = Column('EMAIL', String())
    password = Column('PASSWORD', String())
    # status can be admin or/and user, has to be [] or set()
    _status = Column('STATUS', Integer, default=1)
    wishlist = relationship('Wishlist')
    id = Column(Integer, primary_key=True)
    address = relationship('Address',backref="user",uselist = False)

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self,value):
        self.id = value

    @hybrid_property
    def firstname(self):
        return str(self._firstname).capitalize()


    @firstname.setter
    def firstname(self, value):
        v = value.strip()
        special_characters = '!@#$%^&*()-+?_=,<">/'
        for char in v:
            if char in special_characters:
                raise ValueError('a name cannot contain special characters')
        self._firstname = value

    @hybrid_property
    def lastname(self):
        return str(self._lastname).capitalize()

    @lastname.setter
    def lastname(self, value):
        v = value.strip()
        special_characters = '!@#$%^&*()-+?_=,<">/'
        for char in v:
            if char in special_characters:
                raise ValueError('a name cannot contain special characters')
        self._lastname = value

    @hybrid_property
    def email(self):
        return str(self._email)

    @email.setter
    def email(self, value):
        v = value.strip()
        valid = False
        for char in v:
            if char == '@':
                valid = True
        if valid:
            self._email = value
        else:
            raise ValueError('no valid email')

    @hybrid_property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in status_role.keys():
            self._status = value
        else:
            raise ValueError('no valid status')

    @property
    def __str__(self) -> str:
        return f'{self._firstname} {self._lastname}'
