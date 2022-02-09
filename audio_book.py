from book import Book
from sqlalchemy import Column, String, Time
from sqlalchemy.ext.hybrid import hybrid_property


class AudioBook(Book):
    __tablename__ = "T_AUDIOBOOK"

    _reader_first_name = Column('F_READER_FIRST_NAME', String(1478))
    _reader_last_name = Column('F_READER_LAST_NAME', String(102))
    _reader_middle_name = Column('F_READER_MIDDLE_NAME', String(102))
    duration = Column('F_DURATION', Time)

    @hybrid_property
    def reader_first_name(self) -> str:
        return str(self._reader_first_name).capitalize()

    @reader_first_name.setter
    def reader_first_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('First name is too small')
        # that is the longest existing name
        if len(v) > 1478:
            raise ValueError('First name should be less than 1478 symbols')
        self._reader_first_name = v

    @hybrid_property
    def reader_last_name(self) -> str:
        return str(self._reader_last_name).capitalize()

    @reader_last_name.setter
    def reader_last_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('Last name is too small')
        # that is the longest existing last name
        if len(v) > 102:
            raise ValueError('Last name should be less than 102 symbols')
        self._reader_last_name = v

    @hybrid_property
    def reader_middle_name(self) -> str:
        return str(self._reader_middle_name).capitalize()

    @reader_middle_name.setter
    def reader_middle_name(self, value) -> None:
        v = value.strip()
        if len(v) > 102:
            raise ValueError('Middle name should be less than 102 symbols')
        self._reader_middle_name = v

    @property
    def reader_full_name(self) -> str:
        return f'{self._reader_first_name} {self._reader_middle_name} {self._reader_last_name}'
