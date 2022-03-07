from sqlalchemy import Column, Float, ForeignKey, Integer
from book import Book


class EBook(Book):
    __tablename__ = "T_EBOOK"

    # in MB
    size = Column('F_SIZE', Float)
    id = Column(Integer, ForeignKey('T_Book.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'T_EBOOK'}

