from sqlalchemy.ext.hybrid import hybrid_property

from myapp import db



class User(db.Model):
    __tablename__ = "T_USER"
    id = db.Column('id', db.Integer, primary_key=True, index=True)
    username = db.Column('username', db.String(200))
    email = db.Column('email', db.String(200))
    firstname = db.Column('FIRST_NAME', db.String(50))
    lastname = db.Column('LAST_NAME', db.String(50))
    password = db.Column('PASSWORD', db.String(10))
    # status can be admin or/and user, has to be [] or set()
    status = db.Column('STATUS', db.Integer, default=1)
    wishlist = db.relationship('Wishlist', back_populates="user", uselist=False)
    address = db.relationship('Address', back_populates="user", uselist=False)



class Address(db.Model):
    __tablename__ = "T_ADDRESS"
    id = db.Column('id', db.Integer, primary_key=True, index=True)
    _street = db.Column('STREET', db.String(88))
    _number = db.Column('NUMBER', db.String(10))
    _city = db.Column('CITY', db.String(88))
    _country = db.Column('C0UNTRY', db.String(56))
    _postcode = db.Column('POSTCODE', db.String(30))
    user_id = db.Column('F_USER_ID', db.ForeignKey(User.id), index=True)
    user = db.relationship('User', foreign_keys='Address.user_id', back_populates="address")


    @hybrid_property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @hybrid_property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        v = value.strip()
        special_characters = '!@#$%^&*()-+?_=,<">'
        for char in v:
            if char in special_characters:
                raise ValueError('a number cannot contain special characters')
        self._number = value

    @hybrid_property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @hybrid_property
    def country(self):
        return self._country

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