from config import DB_HOST, DB_PASSWORD, DB_USER_NAME, DB_PORT, DB_NAME
from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create engine
engine = create_engine(f'mysql+mysqlconnector://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
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


def create_database(engine_, do_erase=False):
    from paper_book import PaperBook
    from e_book import EBook
    from audio_book import AudioBook
    from wishlist import Wishlist
    from wishlistbook import WishlistBook
    from user import User
    from book import Book

    """
    create the database
    """
    if do_erase:  # erase the database
        # in case Base.metadata.drop_all(engine) does not work
        # list all tables here  classname.__table__.drop(bind=engine)
        # the issue is the schema which
        PaperBook.__table__.drop(bind=engine_)
        EBook.__table__.drop(bind=engine_)
        AudioBook.__table__.drop(bind=engine_)
        Wishlist.__table__.drop(bind=engine_)
        WishlistBook.__table__.drop(bind=engine_)
        User.__table__.drop(bind=engine_)
        Book.__table__.drop(bind=engine_)

        # Base.metadata.drop_all(bind=engine, tables=[ObjectName.__table__])

    # create tables
    Base.metadata.create_all(engine_)
