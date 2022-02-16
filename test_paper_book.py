from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from paper_book import PaperBook
from constants import categories

C_TITLE = 'Staring at the Sun'
C_INCORRECT_TITLE = str('[i for i in ...]')
C_AUTHOR_LAST_NAME = 'Yalom'
C_AUTHOR_INCORRECT_LAST_NAME_LONG = str('[i for i in ...]')
C_AUTHOR_INCORRECT_LAST_NAME_SHORT = ''
C_AUTHOR_FIRST_NAME = 'Irvin'
C_AUTHOR_INCORRECT_FIRST_NAME_LONG = str('[i for i in ...]')
C_AUTHOR_INCORRECT_FIRST_NAME_SHORT = ''
C_AUTHOR_MIDDLE_NAME = 'David'
C_AUTHOR_INCORRECT_MIDDLE_NAME_LONG = str('[i for i in ...]')
C_AUTHOR_INCORRECT_MIDDLE_NAME_SHORT = ''
C_RELEASE_YEAR = 2008
C_INCORRECT_RELEASE_YEAR_TO_SMALL = 1234
C_INCORRECT_RELEASE_YEAR_TO_BIG = 4321
C_RATING = 9.9
C_INCORRECT_RATING_TO_BIG = 11
C_INCORRECT_RATING_TO_SMALL = -1
C_PIC = '/dsfgasdfgad'
C_CATEGORY = 3
C_INCORRECT_CATEGORY = max(categories.keys()) + 1
C_LANGUAGE = "nl"
C_INCORRECT_LANGUAGE = "ne"
C_ANNOTATION = "Written in Irv Yalom's inimitable story-telling style, Staring at the Sun is a profoundly encouraging" \
               "approach to the universal issue of mortality. In this magisterial opus, capping a lifetime of work and" \
               "personal experience, Dr. Yalom helps us recognize that the fear of death is at the heart of much of " \
               "our anxiety. Such recognition is often catalyzed by an \"awakening experience\"—a dream, \" \
               \"or loss (the death of a loved one, divorce, loss of a job or home), illness, trauma, or aging."
C_INCORRECT_ANNOTATION = str('[i for i in ...]')
C_PUBLISHER = "Wiley"
C_INCORRECT_PUBLISHER = str([1 for i in range(70)])
C_COVER = 1
C_INCORRECT_COVER = 3
C_LENGTH = 15
C_INCORRECT_LENGTH = 301
C_WIDTH = 15
C_INCORRECT_WIDTH = 301
C_WEIGHT = 315
C_INCORRECT_WEIGHT = 10001
C_PAGES = 212
C_INCORRECT_PAGES = 23676
C_ISBN = 1234567890111
C_INCORRECT_ISBN = 1


class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class PaperBookTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_audio_book(self):
        paper_book = PaperBook()
        paper_book.book_title = C_TITLE
        paper_book.author_last_name = C_AUTHOR_LAST_NAME
        paper_book.author_first_name = C_AUTHOR_FIRST_NAME
        paper_book.author_middle_name = C_AUTHOR_MIDDLE_NAME
        paper_book.release_year = C_RELEASE_YEAR
        paper_book.rating = C_RATING
        paper_book.pic = C_PIC
        paper_book.category = C_CATEGORY
        paper_book.language = C_LANGUAGE
        paper_book.annotation = C_ANNOTATION
        paper_book.publisher = C_PUBLISHER
        paper_book.cover = C_COVER
        paper_book.length = C_LENGTH
        paper_book.width = C_WIDTH
        paper_book.weight = C_WEIGHT
        paper_book.pages = C_PAGES
        paper_book.isbn = C_ISBN

        self.session.add(paper_book)
        self.session.commit()

        pb_from_query = self.session.query(PaperBook).get(1)
        self.assertEqual(pb_from_query.book_title, paper_book.book_title)
        self.assertEqual(pb_from_query.author_last_name, paper_book.author_last_name)
        self.assertEqual(pb_from_query.author_first_name, paper_book.author_first_name)
        self.assertEqual(pb_from_query.author_middle_name, paper_book.author_middle_name)
        self.assertEqual(pb_from_query.release_year, paper_book.release_year)
        self.assertEqual(pb_from_query.rating, paper_book.rating)
        self.assertEqual(pb_from_query.pic, paper_book.pic)
        self.assertEqual(pb_from_query.category, paper_book.category)
        self.assertEqual(pb_from_query.language, paper_book.language)
        self.assertEqual(pb_from_query.annotation, paper_book.annotation)
        self.assertEqual(pb_from_query.publisher, paper_book.publisher)


