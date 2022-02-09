import datetime

from database import BaseObj
from sqlalchemy import Column, String, Integer, Float, Text
from sqlalchemy.ext.hybrid import hybrid_property



class Book(BaseObj):
    __abstract__ = True
    _book_title = Column('F_TITLE', String(4805))
    _author_first_name = Column('F_AUTHOR_FIRST_NAME', String(200))
    _author_last_name = Column('F_AUTHOR_LAST_NAME', String(200))
    _author_middle_name = Column('F_AUTHOR_MIDDLE_NAME', String(200))
    _release_year = Column('F_RELEASE_YEAR', Integer)
    _rating = Column('F_RATING', Float)
    # link
    _pic = Column('F_PIC', String(400))
    _category = Column('F_CATEGORY', Integer)
    _language = Column('F_LANGUAGE', String(2))
    _annotation = Column('F_TITLE', Text)
    _publisher = Column('F_AUTHOR', String(200))

    @hybrid_property
    def book_title(self) -> str:
        return str(self._book_title).capitalize()

    @book_title.setter
    def book_title(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('Title is too small')
        # that is the longest existing title
        if len(v) > 4805:
            raise ValueError('Title should be less than 4805 symbols')
        self._book_title = v

    @hybrid_property
    def author_first_name(self) -> str:
        return str(self._author_first_name).capitalize()

    @author_first_name.setter
    def author_first_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('First name is too small')
        # that is the longest existing name
        if len(v) > 1478:
            raise ValueError('First name should be less than 1478 symbols')
        self._author_first_name = v

    @hybrid_property
    def author_last_name(self) -> str:
        return str(self._author_last_name).capitalize()

    @author_last_name.setter
    def author_last_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('Last name is too small')
        # that is the longest existing last name
        if len(v) > 102:
            raise ValueError('Last name should be less than 102 symbols')
        self._author_last_name = v

    @hybrid_property
    def author_middle_name(self) -> str:
        return str(self._author_middle_name).capitalize()

    @author_middle_name.setter
    def author_middle_name(self, value) -> None:
        v = value.strip()
        if len(v) > 102:
            raise ValueError('Middle name should be less than 102 symbols')
        self._author_middle_name = v

    @property
    def author_full_name(self) -> str:
        return f'{self._author_first_name} {self._author_middle_name} {self._author_last_name}'

    @hybrid_property
    def release_year(self) -> int:
        return int(self._release_year)

    @release_year.setter
    def release_year(self, value) -> None:
        v = value
        if v <= 1457:
            raise ValueError('First printed book appeared in 1457 year')
        today_year = datetime.date.year
        if v > today_year:
            raise ValueError(f'Year should be less than {today_year}')
        self._release_year = v

    @property
    def __str__(self) -> str:
        return f'{self._book_title} - {self.author_full_name}'
