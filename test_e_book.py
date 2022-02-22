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
C_RATING_3 = 8.9
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
        self.assertEqual(eb_from_query.book_title, C_TITLE)
        self.assertEqual(eb_from_query.author_last_name, C_AUTHOR_LAST_NAME)
        self.assertEqual(eb_from_query.author_first_name, C_AUTHOR_FIRST_NAME)
        self.assertEqual(eb_from_query.author_middle_name, C_AUTHOR_MIDDLE_NAME)
        self.assertEqual(eb_from_query.release_year, C_RELEASE_YEAR)
        self.assertEqual(eb_from_query.rating, C_RATING)
        self.assertEqual(eb_from_query.pic, C_PIC)
        self.assertEqual(eb_from_query.category, C_CATEGORY)
        self.assertEqual(eb_from_query.language, C_LANGUAGE)
        self.assertEqual(eb_from_query.annotation, C_ANNOTATION)
        self.assertEqual(eb_from_query.publisher, C_PUBLISHER)
        self.assertEqual(eb_from_query.size, C_SIZE)


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
        self.session.add(e_book)
        self.session.commit()
        self.ebook = e_book

    def test_controller_get(self):
        id_eb = self.ebook.id
        eb = self.controller.get_ebook_by_id(id_eb)
        self.assertEqual(eb.book_title, C_TITLE)
        self.assertEqual(eb.author_last_name, C_AUTHOR_LAST_NAME)
        self.assertEqual(eb.author_first_name, C_AUTHOR_FIRST_NAME)
        self.assertEqual(eb.author_middle_name, C_AUTHOR_MIDDLE_NAME)
        self.assertEqual(eb.release_year, C_RELEASE_YEAR)
        self.assertEqual(eb.rating, C_RATING)
        self.assertEqual(eb.pic, C_PIC)
        self.assertEqual(eb.category, C_CATEGORY)
        self.assertEqual(eb.language, C_LANGUAGE)
        self.assertEqual(eb.annotation, C_ANNOTATION)
        self.assertEqual(eb.publisher, C_PUBLISHER)
        self.assertEqual(eb.size, C_SIZE)

    def test_controller_add_book_happy_path(self):
        id_ebook2 = self.controller.add_ebook(C_TITLE_2, C_SIZE_2, C_AUTHOR_FIRST_NAME_2, C_AUTHOR_MIDDLE_NAME_2,
                                              C_AUTHOR_LAST_NAME_2, C_RELEASE_YEAR_2, C_CATEGORY_2, C_LANGUAGE_2,
                                              C_ANNOTATION_2, C_PUBLISHER_2, C_RATING_2, C_PIC_2)
        eb_2 = self.controller.get_ebook_by_id(id_ebook2)

        self.assertEqual(eb_2.book_title, C_TITLE_2)
        self.assertEqual(eb_2.author_last_name, C_AUTHOR_LAST_NAME_2)
        self.assertEqual(eb_2.author_first_name, C_AUTHOR_FIRST_NAME_2)
        self.assertEqual(eb_2.author_middle_name, C_AUTHOR_MIDDLE_NAME_2)
        self.assertEqual(eb_2.release_year, C_RELEASE_YEAR_2)
        self.assertEqual(eb_2.rating, C_RATING_2)
        self.assertEqual(eb_2.pic, C_PIC_2)
        self.assertEqual(eb_2.category, C_CATEGORY_2)
        self.assertEqual(eb_2.language, C_LANGUAGE_2)
        self.assertEqual(eb_2.annotation, C_ANNOTATION_2)
        self.assertEqual(eb_2.publisher, C_PUBLISHER_2)
        self.assertEqual(eb_2.size, C_SIZE_2)

    def test_change_ebook_happy_path(self):
        id_eb = self.ebook.id
        self.controller.change_ebook(id_eb, C_TITLE_2, C_SIZE_2, C_AUTHOR_FIRST_NAME_2, C_AUTHOR_MIDDLE_NAME_2,
                                     C_AUTHOR_LAST_NAME_2, C_RELEASE_YEAR_2, C_CATEGORY_2, C_LANGUAGE_2,
                                     C_ANNOTATION_2, C_PUBLISHER_2, C_RATING_2, C_PIC_2)
        eb_2 = self.controller.get_ebook_by_id(id_eb)

        self.assertEqual(eb_2.book_title, C_TITLE_2)
        self.assertEqual(eb_2.author_last_name, C_AUTHOR_LAST_NAME_2)
        self.assertEqual(eb_2.author_first_name, C_AUTHOR_FIRST_NAME_2)
        self.assertEqual(eb_2.author_middle_name, C_AUTHOR_MIDDLE_NAME_2)
        self.assertEqual(eb_2.release_year, C_RELEASE_YEAR_2)
        self.assertEqual(eb_2.rating, C_RATING_2)
        self.assertEqual(eb_2.pic, C_PIC_2)
        self.assertEqual(eb_2.category, C_CATEGORY_2)
        self.assertEqual(eb_2.language, C_LANGUAGE_2)
        self.assertEqual(eb_2.annotation, C_ANNOTATION_2)
        self.assertEqual(eb_2.publisher, C_PUBLISHER_2)
        self.assertEqual(eb_2.size, C_SIZE_2)

    def test_rate_ebook_happy_path(self):
        self.controller.rate_ebook(self.ebook.id, C_RATING_3)
        saved_rating = self.controller.get_ebook_by_id(self.ebook.id).rating
        self.assertEqual(saved_rating, C_RATING_3)

    def test_remove_book_happy_path(self):
        id_ebook3 = self.controller.add_ebook(C_TITLE_2, C_SIZE_2, C_AUTHOR_FIRST_NAME_2, C_AUTHOR_MIDDLE_NAME_2,
                                              C_AUTHOR_LAST_NAME_2, C_RELEASE_YEAR_2, C_CATEGORY_2, C_LANGUAGE_2,
                                              C_ANNOTATION_2, C_PUBLISHER_2, C_RATING_2, C_PIC_2)
        self.controller.remove_ebook(id_ebook3)
        with self.assertRaises(ValueError):
            self.controller.get_ebook_by_id(id_ebook3)

    def test_get_all_books(self):
        id_ebook3 = self.controller.add_ebook(C_TITLE_2, C_SIZE_2, C_AUTHOR_FIRST_NAME_2, C_AUTHOR_MIDDLE_NAME_2,
                                              C_AUTHOR_LAST_NAME_2, C_RELEASE_YEAR_2, C_CATEGORY_2, C_LANGUAGE_2,
                                              C_ANNOTATION_2, C_PUBLISHER_2, C_RATING_2, C_PIC_2)
        list_with_all_ebooks = self.controller.get_all_ebook()
        self.assertEqual(type(list_with_all_ebooks), list)
        self.assertIn(id_ebook3, list(map(lambda x: x.id, list_with_all_ebooks)))

    def test_get_all_ebook_newest_first(self):
        id_ebook4 = self.controller.add_ebook(C_TITLE_2, C_SIZE_2, C_AUTHOR_FIRST_NAME_2, C_AUTHOR_MIDDLE_NAME_2,
                                              C_AUTHOR_LAST_NAME_2, 1950, C_CATEGORY_2, C_LANGUAGE_2,
                                              C_ANNOTATION_2, C_PUBLISHER_2, C_RATING_2, C_PIC_2)
        id_ebook5 = self.controller.add_ebook(C_TITLE_2, C_SIZE_2, C_AUTHOR_FIRST_NAME_2, C_AUTHOR_MIDDLE_NAME_2,
                                              C_AUTHOR_LAST_NAME_2, 2022, C_CATEGORY_2, C_LANGUAGE_2,
                                              C_ANNOTATION_2, C_PUBLISHER_2, C_RATING_2, C_PIC_2)
        list_with_ebooks = self.controller.get_all_ebook_newest_first()
        # list_with_ebooks = self.controller.get_all_ebook()
        # print(list(map(lambda x: x.release_year, list_with_ebooks)))
        list_with_release_years = list(map(lambda x: x.release_year, list_with_ebooks))
        # print(list_with_release_years)
        self.assertTrue(list_with_release_years[0] >= list_with_release_years[-1])
        self.assertEqual(type(list_with_ebooks), list)

    def test_get_all_ebook_oldest_first(self):
        id_ebook4 = self.controller.add_ebook(C_TITLE_2, C_SIZE_2, C_AUTHOR_FIRST_NAME_2, C_AUTHOR_MIDDLE_NAME_2,
                                              C_AUTHOR_LAST_NAME_2, 1950, C_CATEGORY_2, C_LANGUAGE_2,
                                              C_ANNOTATION_2, C_PUBLISHER_2, C_RATING_2, C_PIC_2)
        id_ebook5 = self.controller.add_ebook(C_TITLE_2, C_SIZE_2, C_AUTHOR_FIRST_NAME_2, C_AUTHOR_MIDDLE_NAME_2,
                                              C_AUTHOR_LAST_NAME_2, 2022, C_CATEGORY_2, C_LANGUAGE_2,
                                              C_ANNOTATION_2, C_PUBLISHER_2, C_RATING_2, C_PIC_2)
        list_with_ebooks = self.controller.get_all_ebook_oldest_first()
        list_with_release_years = list(map(lambda x: x.release_year, list_with_ebooks))
        self.assertTrue(list_with_release_years[0] <= list_with_release_years[-1])
        self.assertEqual(type(list_with_ebooks), list)

    def test_get_ebook_by_title(self):
        list_with_ebooks = self.controller.get_ebook_by_title(C_TITLE)
        list_with_titles = list(map(lambda x: x.book_title, list_with_ebooks))
        self.assertIn(C_TITLE, list_with_titles)

    def test_get_ebook_by_author_last_name(self):
        list_with_ebooks = self.controller.get_ebook_by_author_last_name(C_AUTHOR_LAST_NAME)
        list_with_last_names = list(map(lambda x: x.author_last_name, list_with_ebooks))
        self.assertIn(C_AUTHOR_LAST_NAME, list_with_last_names)

    def test_get_ebook_by_category(self):
        list_with_ebooks = self.controller.get_ebook_by_category(C_CATEGORY)
        list_with_categories = list(map(lambda x: x.category, list_with_ebooks))
        self.assertIn(C_CATEGORY, list_with_categories)

    def test_get_ebook_by_release_year(self):
        list_with_ebooks = self.controller.get_ebook_by_release_year(C_RELEASE_YEAR)
        list_with_categories = list(map(lambda x: x.release_year, list_with_ebooks))
        self.assertIn(C_RELEASE_YEAR, list_with_categories)

    def test_get_ebook_by_publisher(self):
        list_with_ebooks = self.controller.get_ebook_by_publisher(C_PUBLISHER)
        list_with_publishers = list(map(lambda x: x.publisher, list_with_ebooks))
        self.assertIn(C_PUBLISHER, list_with_publishers)

    def test_get_ebook_by_rating(self):
        list_with_ebooks = self.controller.get_ebook_by_rating(8, 10)
        list_with_ratings = list(map(lambda x: x.rating, list_with_ebooks))
        self.assertIn(C_RATING, list_with_ratings)