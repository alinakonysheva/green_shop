from sqlalchemy import Column, Float
from book import Book


class EBook(Book):
    __tablename__ = "T_EBOOK"

    # in MB
    size = Column('F_SIZE', Float)

