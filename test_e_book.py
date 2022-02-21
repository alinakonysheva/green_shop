from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from e_book import EBook
from constants import categories
from controller_ebook import ControllerEBook

C_TITLE = 'Staring at the Sun'
C_TITLE_2 = 'Staring at the Sun2'
C_INCORRECT_TITLE = str('[i for i in ...]')
C_AUTHOR_LAST_NAME = 'Yalom'
C_AUTHOR_LAST_NAME_2 = 'Yalom2'
C_AUTHOR_INCORRECT_LAST_NAME_LONG = str('[i for i in ...]')
C_AUTHOR_INCORRECT_LAST_NAME_SHORT = ''
C_AUTHOR_FIRST_NAME = 'Irvin'
C_AUTHOR_FIRST_NAME_2 = 'Irvin2'
C_AUTHOR_INCORRECT_FIRST_NAME_LONG = str('[i for i in ...]')
C_AUTHOR_INCORRECT_FIRST_NAME_SHORT = ''
C_AUTHOR_MIDDLE_NAME = 'David'
C_AUTHOR_MIDDLE_NAME_2 = 'David_2'
C_AUTHOR_INCORRECT_MIDDLE_NAME_LONG = str('[i for i in ...]')
C_AUTHOR_INCORRECT_MIDDLE_NAME_SHORT = ''
C_RELEASE_YEAR = 2008
C_RELEASE_YEAR_2 = 2010
C_INCORRECT_RELEASE_YEAR_TO_SMALL = 1234
C_INCORRECT_RELEASE_YEAR_TO_BIG = 4321
C_RATING = 9.9
C_RATING_2 = 10.0
C_INCORRECT_RATING_TO_BIG = 11
C_INCORRECT_RATING_TO_SMALL = -1
C_PIC = '/dsfgasdfgad'
C_PIC_2 = '/dsfgasdfgad2'
C_CATEGORY = 3
C_CATEGORY_2 = 5
C_INCORRECT_CATEGORY = max(categories.keys()) + 1
C_LANGUAGE = "nl"
C_LANGUAGE_2 = "ru"
C_INCORRECT_LANGUAGE = "ne"
C_ANNOTATION = "Written in Irv Yalom's inimitable story-telling style, Staring at the Sun is a profoundly encouraging" \
               "approach to the universal issue of mortality. In this magisterial opus, capping a lifetime of work and" \
               "personal experience, Dr. Yalom helps us recognize that the fear of death is at the heart of much of " \
               "our anxiety. Such recognition is often catalyzed by an \"awakening experience\"—a dream, \" \
               \"or loss (the death of a loved one, divorce, loss of a job or home), illness, trauma, or aging."
C_ANNOTATION_2 = "Written in Irv Yalom's inimitable story-telling style, Staring at the Sun is a profoundly encouraging" \
                 "approach to the universal issue of mortality. In this magisterial opus, capping a lifetime of work and" \
                 "personal experience, Dr. Yalom helps us recognize that the fear of death is at the heart of much of " \
                 "our anxiety. Such recognition is often catalyzed by an \"awakening experience\"—a dream, \" \
                 \"or loss (the death of a loved one, divorce, loss of a job or home), illness, trauma, or aging.2"
C_INCORRECT_ANNOTATION = str('[i for i in ...]')
C_PUBLISHER = "Wiley"
C_PUBLISHER_2 = "Wiley2"
C_INCORRECT_PUBLISHER = str([1 for i in range(70)])
C_SIZE = 56.0
C_SIZE_2 = 58.0


class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class EBookTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_e_book_happy_path(self):
        e_book = EBook()
        e_book.book_title = C_TITLE
        e_book.author_last_name = C_AUTHOR_LAST_NAME
        e_book.author_first_name = C_AUTHOR_FIRST_NAME
        e_book.author_middle_name = C_AUTHOR_MIDDLE_NAME
        e_book.release_year = C_RELEASE_YEAR
        e_book.rating = C_RATING
        e_book.pic = C_PIC
        e_book.category = C_CATEGORY
        e_book.language = C_LANGUAGE
        e_book.annotation = C_ANNOTATION
        e_book.publisher = C_PUBLISHER
        e_book.size = C_SIZE

        self.session.add(e_book)
        self.session.commit()

        eb_from_query = self.session.query(EBook).get(1)
        self.assertEqual(eb_from_query.book_title, e_book.book_title)
        self.assertEqual(eb_from_query.author_last_name, e_book.author_last_name)
        self.assertEqual(eb_from_query.author_first_name, e_book.author_first_name)
        self.assertEqual(eb_from_query.author_middle_name, e_book.author_middle_name)
        self.assertEqual(eb_from_query.release_year, e_book.release_year)
        self.assertEqual(eb_from_query.rating, e_book.rating)
        self.assertEqual(eb_from_query.pic, e_book.pic)
        self.assertEqual(eb_from_query.category, e_book.category)
        self.assertEqual(eb_from_query.language, e_book.language)
        self.assertEqual(eb_from_query.annotation, e_book.annotation)
        self.assertEqual(eb_from_query.publisher, e_book.publisher)
        self.assertEqual(eb_from_query.size, e_book.size)


class EBookControllerTests(BaseDbTest):
    def do_setup(self):
        e_book = EBook()
        e_book.book_title = C_TITLE
        e_book.author_last_name = C_AUTHOR_LAST_NAME
        e_book.author_first_name = C_AUTHOR_FIRST_NAME
        e_book.author_middle_name = C_AUTHOR_MIDDLE_NAME
        e_book.release_year = C_RELEASE_YEAR
        e_book.rating = C_RATING
        e_book.pic = C_PIC
        e_book.category = C_CATEGORY
        e_book.language = C_LANGUAGE
        e_book.annotation = C_ANNOTATION
        e_book.publisher = C_PUBLISHER
        e_book.size = C_SIZE
        self.controller = ControllerEBook(self.session)


    def test_controller_get(self):
        # не надо так делать
        # ADD должен возвращть id
        eb = self.controller.get_ebook_by_id(1)
        self.assertEqual(eb.book_title, self.e_book.book_title)
        self.assertEqual(eb.author_last_name, self.e_book.author_last_name)
        self.assertEqual(eb.author_first_name, self.e_book.author_first_name)
        self.assertEqual(eb.author_middle_name, self.e_book.author_middle_name)
        self.assertEqual(eb.release_year, self.e_book.release_year)
        self.assertEqual(eb.rating, self.e_book.rating)
        self.assertEqual(eb.pic, self.e_book.pic)
        self.assertEqual(eb.category, self.e_book.category)
        self.assertEqual(eb.language, self.e_book.language)
        self.assertEqual(eb.annotation, self.e_book.annotation)
        self.assertEqual(eb.publisher, self.e_book.publisher)
        self.assertEqual(eb.size, self.e_book.size)

    def test_controller_add_book_happy_path(self):
        self.controller.add_ebook(C_TITLE_2, C_SIZE_2, C_AUTHOR_FIRST_NAME_2, C_AUTHOR_MIDDLE_NAME_2,
                                  C_AUTHOR_LAST_NAME_2,
                                  C_RELEASE_YEAR_2, C_CATEGORY_2, C_LANGUAGE_2, C_ANNOTATION_2,
                                  C_PUBLISHER_2, C_RATING_2,
                                  C_PIC_2)

        self.assertEqual(len(self.controller.get_all_ebook()), 1)

        #eb_from_query = self.session.query(EBook).get(2)
        #self.assertEqual(eb_from_query.size, C_SIZE_2)
