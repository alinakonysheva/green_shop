from sqlalchemy.orm import relationship, declared_attr

from database import BaseObj
from user import User
from sqlalchemy import Column, ForeignKey


class Wishlist(BaseObj):
    __tablename__ = "T_WISHLIST"

    id_user = Column('F_USER_ID', ForeignKey(User.id))
    user = relationship(User, foreign_keys='Wishlist.id_user', back_populates="wishlist")

    @declared_attr
    def books(cls):
        return relationship('WishlistBook', back_populates='wishlist')

    # books = relationship('WishlistBook', back_populates='wishlist'
