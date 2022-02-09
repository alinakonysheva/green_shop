from sqlalchemy import Column, String, Time, Integer
from sqlalchemy.ext.hybrid import hybrid_property
from book import Book
from constants import covers


class PaperBook(Book):
    __tablename__ = "T_PAPER_BOOK"

    _cover = Column('F_COVER', Integer)
    # in cm
    _length = Column('F_LENGTH', Integer)
    # in cm
    _width = Column('F_WIDTH', Integer)
    # in g
    _weight = Column('F_WEIGHT', Integer)
    _pages = Column('F_PAGES', Integer)
    _isbn = Column('F_ISBN', Integer)

    @hybrid_property
    def cover(self) -> int:
        return int(self._cover)

    @cover.setter
    def cover(self, value) -> None:
        if value in covers.keys():
            self._cover = value
        else:
            raise ValueError(f'Cover has to be one of values {covers.keys()}')

    @hybrid_property
    def length(self) -> int:
        return int(self._length)

    @length.setter
    def length(self, value: int) -> None:
        # the longest existing book
        if value > 300:
            raise ValueError('the length of the book can not be longer than 3m')

        if value <= 0:
            raise ValueError('the length of the book can not be 0 of negative')

        self._length = value

    @hybrid_property
    def width(self) -> int:
        return int(self._width)

    @width.setter
    def width(self, value: int) -> None:
        # the widest existing book
        if value > 300:
            raise ValueError('the width of the book can not be longer than 3m')

        if value <= 0:
            raise ValueError('the width of the book can not be 0 of negative')

        self._width = value

    # pages
    @hybrid_property
    def pages(self) -> int:
        return int(self._pages)

    @pages.setter
    def pages(self, value: int) -> None:
        # the widest existing book
        if value > 23675:
            raise ValueError('the pages of the book can not be more than 23675')

        if value <= 0:
            raise ValueError('the pages of the book can not be 0 of negative')

        self._pages = value

    # isbn
    @hybrid_property
    def isbn(self) -> int:
        return int(self._isbn)

    @isbn.setter
    def isbn(self, value: int) -> None:
        if len(str(value)) != 13:
            raise ValueError('the isbn of the book can not be longer than 13 digit')

        self._isbn = value
