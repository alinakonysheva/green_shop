from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

from constants import categories, languages
from database import Base
from sqlalchemy import Column, String, Integer, Float, Text, ForeignKey


class Book(Base):
    __tablename__ = 'T_Book'
    id = Column(Integer, primary_key=True)
    _title = Column('F_TITLE', String(200))
    _author_first_name = Column('F_AUTHOR_FIRST_NAME', String(1478))
    _author_last_name = Column('F_AUTHOR_LAST_NAME', String(102))
    _author_middle_name = Column('F_AUTHOR_MIDDLE_NAME', String(102))
    _release_year = Column('F_RELEASE_YEAR', Integer)
    _rating = Column('F_RATING', Float)
    # link
    _pic = Column('F_PIC', String(400))
    _category = Column('F_CATEGORY', Integer)
    _language = Column('F_LANGUAGE', String(2))
    _annotation = Column('F_ANNOTATION', Text)
    _publisher = Column('F_PUBLISHER', String(200))
    @declared_attr
    def wishlists(cls):
        return relationship('WishlistBook', back_populates='book')

    # wishlists = relationship('WishlistBook', back_populates='book')

    @hybrid_property
    def book_title(self) -> str:
        return str(self._title).capitalize()

    @book_title.setter
    def book_title(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('Title is too small')
        # that is the longest existing title
        if len(v) > 4805:
            raise ValueError('Title should be less than 4805 symbols')
        self._title = v

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

    @hybrid_property
    def pic(self) -> str:
        return f'{self._pic}'

    @pic.setter
    def pic(self, value) -> None:
        if len(value) > 400:
            raise ValueError('Link should be less than 400 symbols')
        if value == '':
            raise ValueError('Link can not be empty')
        self._pic = value

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
        today_year = datetime.today().year
        if v > today_year:
            raise ValueError(f'Year should be less than {today_year}')
        self._release_year = v

    @hybrid_property
    def rating(self) -> float:
        return float(self._rating)

    @rating.setter
    def rating(self, value) -> None:
        v = value
        if v < 0:
            raise ValueError('Rating should be positive number')
        if v > 10:
            raise ValueError(f'Rating should be less than 10')
        self._rating = v

    @hybrid_property
    def category(self) -> int:
        return int(self._rating)

    @category.setter
    def category(self, value) -> None:
        v = value
        category_options = categories.keys()
        if v in category_options:
            self._category = v
        else:
            raise ValueError(f'category should be in between {min(category_options)} and {max(category_options)}')

    @hybrid_property
    def language(self) -> str:
        return str(self._language)

    @language.setter
    def language(self, value) -> None:
        v = value
        if len(v) != 2:
            raise ValueError('Language should be set with 2 letters')
        if v in languages.keys():
            self._language = v
        else:
            raise ValueError('Language should be set with 2 existing abbreviation letters')

    @hybrid_property
    def annotation(self) -> str:
        return str(self._annotation)

    @annotation.setter
    def annotation(self, value) -> None:
        self._annotation = value

    @hybrid_property
    def publisher(self) -> str:
        return str(self._publisher).capitalize()

    @publisher.setter
    def publisher(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('the name of the publisher is too small')
        if len(v) > 200:
            raise ValueError('the name of the publisher should be less than 200 symbols')
        self._publisher = v

    @property
    def __str__(self) -> str:
        return f'{self._book_title} - {self.author_full_name}'
