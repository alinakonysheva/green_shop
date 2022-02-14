from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import BaseObj
from book import Book
from wishlist import Wishlist


class WishlistBook(BaseObj):
    __tablename__ = 'T_WISHLISTBOOK'

    id_book = Column('id_book', ForeignKey(Book.id))
    id_wishlist = Column('id_wishlist', ForeignKey(Wishlist.id))

    book = relationship(Book, back_populates='wishlists')
    wishlist = relationship(Wishlist, back_populates='books')

    # __mapper_args__ = {'polymorphic_identity': 'T_WISHLISTBOOK', 'concrete': True}

    def __str__(self) -> str:
        return f'{self.id} - {self.id_book} - {self.id_wishlist} '
