from config import HOST, PASSWORD, USER_NAME, PORT
from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create engine
engine = create_engine(f'mysql+mysqlconnector://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/acteursfilms')
# create connection to database
engine.connect()

# create a session by linking the engine
Session = sessionmaker(bind=engine)
session = Session()

# needed for declaring tables
Base = declarative_base()


class BaseObj(Base):
    __abstract__ = True

    id = Column('PK_ID', Integer, primary_key=True, index=True)
    # TODO: add created, updated


def create_database(engine, do_erase=False):
    from paper_book import PaperBook
    from e_book import EBook
    from audio_book import AudioBook

    """
    create the database
    """
    if do_erase is True:  # erase the database
        # in case Base.metadata.drop_all(engine) does not work
        # list all tables here  classname.__table__.drop(bind=engine)
        # the issue is the schema which
        PaperBook.__table__.drop(bind=engine)
        EBook.__table__.drop(bind=engine)
        AudioBook.__table__.drop(bind=engine)

        # Base.metadata.drop_all(bind=engine, tables=[ObjectName.__table__])

    # create tables
    Base.metadata.create_all(engine)
