from book import Book
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property


class AudioBook(Book):
    __tablename__ = "T_AUDIOBOOK"

    _reader_first_name = Column('F_READER_FIRST_NAME', String(100))
    _reader_last_name = Column('F_READER_LAST_NAME', String(100))
    _reader_middle_name = Column('F_READER_MIDDLE_NAME', String(100))
    _duration_hours = Column('F_DURATION_HOURS', Integer)
    _duration_minutes = Column('F_DURATION_MINUTES', Integer)
    _duration_seconds = Column('F_DURATION_SECONDS', Integer)
    __mapper_args__ = {'polymorphic_identity': 'T_AUDIOBOOK'}
    id = Column(Integer, ForeignKey('T_Book.id'), primary_key=True)

    @hybrid_property
    def reader_first_name(self) -> str:
        return str(self._reader_first_name).capitalize()

    @reader_first_name.setter
    def reader_first_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('First name is too small')
        if len(v) > 100:
            raise ValueError('First name should be less than 100 symbols')
        self._reader_first_name = v

    @hybrid_property
    def reader_last_name(self) -> str:
        return str(self._reader_last_name).capitalize()

    @reader_last_name.setter
    def reader_last_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('Last name is too small')
        if len(v) > 100:
            raise ValueError('Last name should be less than 100 symbols')
        self._reader_last_name = v

    @hybrid_property
    def reader_middle_name(self) -> str:
        return str(self._reader_middle_name).capitalize()

    @reader_middle_name.setter
    def reader_middle_name(self, value) -> None:
        v = value.strip()
        if len(v) > 100:
            raise ValueError('Middle name should be less than 100 symbols')
        self._reader_middle_name = v

    @hybrid_property
    def duration_hours(self) -> int:
        return self._duration_hours

    @duration_hours.setter
    def duration_hours(self, value) -> None:
        if value < 0:
            raise ValueError('duration hours have to be positive or 0')
        self._duration_hours = value

    @hybrid_property
    def duration_minutes(self) -> int:
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, value) -> None:
        if value < 0:
            raise ValueError('duration minutes have to be positive or 0')
        if value >= 60:
            raise ValueError('duration minutes have to be less than 60')
        self._duration_minutes = value

    @hybrid_property
    def duration_seconds(self) -> int:
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, value) -> None:
        if value < 0:
            raise ValueError('duration seconds have to be positive or 0')
        if value >= 60:
            raise ValueError('duration seconds have to be less than 60')

        self._duration_seconds = value
