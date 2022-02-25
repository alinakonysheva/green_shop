from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from audio_book import AudioBook
from controller_audio_book import ControllerAudioBook
from constants import categories

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
C_READER_LAST_NAME = 'Smith'
C_READER_LAST_NAME_2 = 'Smith2'
C_READER_INCORRECT_LAST_NAME_LONG = str('[i for i in ...]')
C_READER_INCORRECT_LAST_NAME_SHORT = ''
C_READER_FIRST_NAME = 'Black'
C_READER_FIRST_NAME_2 = 'Black2'
C_READER_INCORRECT_FIRST_NAME_LONG = str('[i for i in ...]')
C_READER_INCORRECT_FIRST_NAME_SHORT = ''
C_READER_MIDDLE_NAME = 'Nil'
C_READER_MIDDLE_NAME_2 = 'Nil2'
C_READER_INCORRECT_MIDDLE_NAME_LONG = str('[i for i in ...]')
C_READER_INCORRECT_MIDDLE_NAME_SHORT = ''
C_DURATION_HOURS = 2
C_DURATION_HOURS_2 = 4
C_DURATION_MINUTES = 50
C_DURATION_MINUTES_2 = 52
C_DURATION_SECONDS = 34
C_DURATION_SECONDS_2 = 36


class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class AudioBookTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_audio_book(self):
        audio_book = AudioBook()
        audio_book.book_title = C_TITLE
        audio_book.author_last_name = C_AUTHOR_LAST_NAME
        audio_book.author_first_name = C_AUTHOR_FIRST_NAME
        audio_book.author_middle_name = C_AUTHOR_MIDDLE_NAME
        audio_book.release_year = C_RELEASE_YEAR
        audio_book.rating = C_RATING
        audio_book.pic = C_PIC
        audio_book.category = C_CATEGORY
        audio_book.language = C_LANGUAGE
        audio_book.annotation = C_ANNOTATION
        audio_book.publisher = C_PUBLISHER
        audio_book.reader_first_name = C_READER_FIRST_NAME
        audio_book.reader_middle_name = C_READER_MIDDLE_NAME
        audio_book.reader_last_name = C_READER_LAST_NAME
        audio_book.duration_hours = C_DURATION_HOURS
        audio_book.duration_minutes = C_DURATION_MINUTES
        audio_book.duration_seconds = C_DURATION_SECONDS

        self.session.add(audio_book)
        self.session.commit()

        ab_from_query = self.session.query(AudioBook).get(1)
        self.assertEqual(ab_from_query.book_title, C_TITLE)
        self.assertEqual(ab_from_query.author_last_name, C_AUTHOR_LAST_NAME)
        self.assertEqual(ab_from_query.author_first_name, C_AUTHOR_FIRST_NAME)
        self.assertEqual(ab_from_query.author_middle_name, C_AUTHOR_MIDDLE_NAME)
        self.assertEqual(ab_from_query.release_year, C_RELEASE_YEAR)
        self.assertEqual(ab_from_query.rating, C_RATING)
        self.assertEqual(ab_from_query.pic, C_PIC)
        self.assertEqual(ab_from_query.category, C_CATEGORY)
        self.assertEqual(ab_from_query.language, C_LANGUAGE)
        self.assertEqual(ab_from_query.annotation, C_ANNOTATION)
        self.assertEqual(ab_from_query.publisher, C_PUBLISHER)
        self.assertEqual(ab_from_query.reader_first_name, C_READER_FIRST_NAME)
        self.assertEqual(ab_from_query.reader_middle_name, C_READER_MIDDLE_NAME)
        self.assertEqual(ab_from_query.reader_last_name, C_READER_LAST_NAME)
        self.assertEqual(ab_from_query.duration_hours, C_DURATION_HOURS)
        self.assertEqual(ab_from_query.duration_minutes, C_DURATION_MINUTES)
        self.assertEqual(ab_from_query.duration_seconds, C_DURATION_SECONDS)

    class ControllerAudioBookTests(BaseDbTest):
        def do_setup(self):
            a_book = AudioBook()
            a_book.book_title = C_TITLE
            a_book.author_last_name = C_AUTHOR_LAST_NAME
            a_book.author_first_name = C_AUTHOR_FIRST_NAME
            a_book.author_middle_name = C_AUTHOR_MIDDLE_NAME
            a_book.release_year = C_RELEASE_YEAR
            a_book.rating = C_RATING
            a_book.pic = C_PIC
            a_book.category = C_CATEGORY
            a_book.language = C_LANGUAGE
            a_book.annotation = C_ANNOTATION
            a_book.publisher = C_PUBLISHER
            a_book.reader_first_name = C_READER_FIRST_NAME
            a_book.reader_middle_name = C_READER_MIDDLE_NAME
            a_book.reader_last_name = C_READER_LAST_NAME
            a_book.duration_hours = C_DURATION_HOURS
            a_book.duration_minutes = C_DURATION_MINUTES
            a_book.duration_seconds = C_DURATION_SECONDS
            self.controller = ControllerAudioBook(self.session)
            self.session.add(a_book)
            self.session.commit()
            self.a_book = a_book

        def test_controller_get_book(self):
            id_ab = self.a_book.id
            ab = self.controller.get_audiobook_by_id(id_ab)
            self.assertEqual(ab.book_title, C_TITLE)
            self.assertEqual(ab.author_last_name, C_AUTHOR_LAST_NAME)
            self.assertEqual(ab.author_first_name, C_AUTHOR_FIRST_NAME)
            self.assertEqual(ab.author_middle_name, C_AUTHOR_MIDDLE_NAME)
            self.assertEqual(ab.release_year, C_RELEASE_YEAR)
            self.assertEqual(ab.rating, C_RATING)
            self.assertEqual(ab.pic, C_PIC)
            self.assertEqual(ab.category, C_CATEGORY)
            self.assertEqual(ab.language, C_LANGUAGE)
            self.assertEqual(ab.annotation, C_ANNOTATION)
            self.assertEqual(ab.publisher, C_PUBLISHER)
            self.assertEqual(ab.reader_first_name, C_READER_FIRST_NAME)
            self.assertEqual(ab.reader_middle_name, C_READER_MIDDLE_NAME)
            self.assertEqual(ab.reader_last_name, C_READER_LAST_NAME)
            self.assertEqual(ab.duration_hours, C_DURATION_HOURS)
            self.assertEqual(ab.duration_minutes, C_DURATION_MINUTES)
            self.assertEqual(ab.duration_seconds, C_DURATION_SECONDS)

        def test_controller_add_book_happy_path(self):
            id_a_book2 = self.controller.add_audiobook(C_TITLE_2, C_READER_FIRST_NAME_2, C_READER_LAST_NAME_2,
                                                       C_READER_MIDDLE_NAME_2, C_DURATION_HOURS_2, C_DURATION_MINUTES_2,
                                                       C_DURATION_SECONDS_2, C_AUTHOR_FIRST_NAME_2,
                                                       C_AUTHOR_MIDDLE_NAME_2, C_AUTHOR_LAST_NAME_2, C_RELEASE_YEAR_2,
                                                       C_CATEGORY_2, C_LANGUAGE_2, C_ANNOTATION_2, C_PUBLISHER_2,
                                                       C_RATING_2, C_PIC_2)
            ab_2 = self.controller.get_audiobook_by_id(id_a_book2)

            self.assertEqual(ab_2.book_title, C_TITLE_2)
            self.assertEqual(ab_2.author_last_name, C_AUTHOR_LAST_NAME_2)
            self.assertEqual(ab_2.author_first_name, C_AUTHOR_FIRST_NAME_2)
            self.assertEqual(ab_2.author_middle_name, C_AUTHOR_MIDDLE_NAME_2)
            self.assertEqual(ab_2.release_year, C_RELEASE_YEAR_2)
            self.assertEqual(ab_2.rating, C_RATING_2)
            self.assertEqual(ab_2.pic, C_PIC_2)
            self.assertEqual(ab_2.category, C_CATEGORY_2)
            self.assertEqual(ab_2.language, C_LANGUAGE_2)
            self.assertEqual(ab_2.annotation, C_ANNOTATION_2)
            self.assertEqual(ab_2.publisher, C_PUBLISHER_2)
            self.assertEqual(ab_2.reader_first_name, C_READER_FIRST_NAME_2)
            self.assertEqual(ab_2.reader_middle_name, C_READER_MIDDLE_NAME_2)
            self.assertEqual(ab_2.reader_last_name, C_READER_LAST_NAME_2)
            self.assertEqual(ab_2.duration_hours, C_DURATION_HOURS_2)
            self.assertEqual(ab_2.duration_minutes, C_DURATION_MINUTES_2)
            self.assertEqual(ab_2.duration_seconds, C_DURATION_SECONDS_2)

        def test_change_audio_book_happy_path(self):
            id_ab = self.a_book.id
            self.controller.change_audiobook(id_ab, C_TITLE_2, C_READER_FIRST_NAME_2, C_READER_LAST_NAME_2,
                                             C_READER_MIDDLE_NAME_2, C_DURATION_HOURS_2, C_DURATION_MINUTES_2,
                                             C_DURATION_SECONDS_2, C_AUTHOR_FIRST_NAME_2,
                                             C_AUTHOR_MIDDLE_NAME_2, C_AUTHOR_LAST_NAME_2, C_RELEASE_YEAR_2,
                                             C_CATEGORY_2, C_LANGUAGE_2, C_ANNOTATION_2, C_PUBLISHER_2,
                                             C_RATING_2, C_PIC_2)
            ab_2 = self.controller.get_audiobook_by_id(id_ab)

            self.assertEqual(ab_2.book_title, C_TITLE_2)
            self.assertEqual(ab_2.author_last_name, C_AUTHOR_LAST_NAME_2)
            self.assertEqual(ab_2.author_first_name, C_AUTHOR_FIRST_NAME_2)
            self.assertEqual(ab_2.author_middle_name, C_AUTHOR_MIDDLE_NAME_2)
            self.assertEqual(ab_2.release_year, C_RELEASE_YEAR_2)
            self.assertEqual(ab_2.rating, C_RATING_2)
            self.assertEqual(ab_2.pic, C_PIC_2)
            self.assertEqual(ab_2.category, C_CATEGORY_2)
            self.assertEqual(ab_2.language, C_LANGUAGE_2)
            self.assertEqual(ab_2.annotation, C_ANNOTATION_2)
            self.assertEqual(ab_2.publisher, C_PUBLISHER_2)
            self.assertEqual(ab_2.reader_first_name, C_READER_FIRST_NAME_2)
            self.assertEqual(ab_2.reader_middle_name, C_READER_MIDDLE_NAME_2)
            self.assertEqual(ab_2.reader_last_name, C_READER_LAST_NAME_2)
            self.assertEqual(ab_2.duration_hours, C_DURATION_HOURS_2)
            self.assertEqual(ab_2.duration_minutes, C_DURATION_MINUTES_2)
            self.assertEqual(ab_2.duration_seconds, C_DURATION_SECONDS_2)

        def test_rate_audiobook_happy_path(self):
            self.controller.rate_audiobook(self.a_book.id, C_RATING_3)
            saved_rating = self.controller.get_audiobook_by_id(self.a_book.id).rating
            self.assertEqual(saved_rating, C_RATING_3)

        def test_remove_book_happy_path(self):
            id_a_book3 = self.controller.add_audiobook(C_TITLE_2, C_READER_FIRST_NAME_2, C_READER_LAST_NAME_2,
                                                       C_READER_MIDDLE_NAME_2, C_DURATION_HOURS_2, C_DURATION_MINUTES_2,
                                                       C_DURATION_SECONDS_2, C_AUTHOR_FIRST_NAME_2,
                                                       C_AUTHOR_MIDDLE_NAME_2, C_AUTHOR_LAST_NAME_2, C_RELEASE_YEAR_2,
                                                       C_CATEGORY_2, C_LANGUAGE_2, C_ANNOTATION_2, C_PUBLISHER_2,
                                                       C_RATING_2, C_PIC_2)
            self.controller.remove_audiobook(id_a_book3)
            with self.assertRaises(ValueError):
                self.controller.get_audiobook_by_id(id_a_book3)

        def test_get_all_paper_book(self):
            id_a_book4 = self.controller.add_audiobook(C_TITLE_2, C_READER_FIRST_NAME_2, C_READER_LAST_NAME_2,
                                                       C_READER_MIDDLE_NAME_2, C_DURATION_HOURS_2, C_DURATION_MINUTES_2,
                                                       C_DURATION_SECONDS_2, C_AUTHOR_FIRST_NAME_2,
                                                       C_AUTHOR_MIDDLE_NAME_2, C_AUTHOR_LAST_NAME_2, C_RELEASE_YEAR_2,
                                                       C_CATEGORY_2, C_LANGUAGE_2, C_ANNOTATION_2, C_PUBLISHER_2,
                                                       C_RATING_2, C_PIC_2)
            list_with_all_a_books = self.controller.get_all_audiobook()
            self.assertEqual(type(list_with_all_a_books), list)
            self.assertIn(id_a_book4, list(map(lambda x: x.id, list_with_all_a_books)))

        def test_get_all_audiobook_newest_first(self):
            id_a_book5 = self.controller.add_audiobook(C_TITLE_2, C_READER_FIRST_NAME_2, C_READER_LAST_NAME_2,
                                                       C_READER_MIDDLE_NAME_2, C_DURATION_HOURS_2, C_DURATION_MINUTES_2,
                                                       C_DURATION_SECONDS_2, C_AUTHOR_FIRST_NAME_2,
                                                       C_AUTHOR_MIDDLE_NAME_2, C_AUTHOR_LAST_NAME_2, 1958,
                                                       C_CATEGORY_2, C_LANGUAGE_2, C_ANNOTATION_2, C_PUBLISHER_2,
                                                       C_RATING_2, C_PIC_2)
            id_a_book6 = self.controller.add_audiobook(C_TITLE_2, C_READER_FIRST_NAME_2, C_READER_LAST_NAME_2,
                                                       C_READER_MIDDLE_NAME_2, C_DURATION_HOURS_2, C_DURATION_MINUTES_2,
                                                       C_DURATION_SECONDS_2, C_AUTHOR_FIRST_NAME_2,
                                                       C_AUTHOR_MIDDLE_NAME_2, C_AUTHOR_LAST_NAME_2, 2022,
                                                       C_CATEGORY_2, C_LANGUAGE_2, C_ANNOTATION_2, C_PUBLISHER_2,
                                                       C_RATING_2, C_PIC_2)
            list_with_a_books = self.controller.get_all_audiobook_newest_first()
            list_with_release_years = list(map(lambda x: x.release_year, list_with_a_books))
            self.assertTrue(list_with_release_years[0] >= list_with_release_years[-1])
            self.assertEqual(type(list_with_a_books), list)

        def test_get_all_audiobook_oldest_first(self):
            id_a_book5 = self.controller.add_audiobook(C_TITLE_2, C_READER_FIRST_NAME_2, C_READER_LAST_NAME_2,
                                                       C_READER_MIDDLE_NAME_2, C_DURATION_HOURS_2, C_DURATION_MINUTES_2,
                                                       C_DURATION_SECONDS_2, C_AUTHOR_FIRST_NAME_2,
                                                       C_AUTHOR_MIDDLE_NAME_2, C_AUTHOR_LAST_NAME_2, 1958,
                                                       C_CATEGORY_2, C_LANGUAGE_2, C_ANNOTATION_2, C_PUBLISHER_2,
                                                       C_RATING_2, C_PIC_2)
            id_a_book6 = self.controller.add_audiobook(C_TITLE_2, C_READER_FIRST_NAME_2, C_READER_LAST_NAME_2,
                                                       C_READER_MIDDLE_NAME_2, C_DURATION_HOURS_2, C_DURATION_MINUTES_2,
                                                       C_DURATION_SECONDS_2, C_AUTHOR_FIRST_NAME_2,
                                                       C_AUTHOR_MIDDLE_NAME_2, C_AUTHOR_LAST_NAME_2, 2022,
                                                       C_CATEGORY_2, C_LANGUAGE_2, C_ANNOTATION_2, C_PUBLISHER_2,
                                                       C_RATING_2, C_PIC_2)
            list_with_a_books = self.controller.get_all_audiobook_oldest_first()
            list_with_release_years = list(map(lambda x: x.release_year, list_with_a_books))
            self.assertTrue(list_with_release_years[0] <= list_with_release_years[-1])
            self.assertEqual(type(list_with_a_books), list)

        def test_get_audiobook_by_title(self):
            list_with_a_books = self.controller.get_audiobook_by_title(C_TITLE)
            list_with_titles = list(map(lambda x: x.book_title, list_with_a_books))
            self.assertIn(C_TITLE, list_with_titles)

        def test_get_audiobook_by_author_last_name(self):
            list_with_a_books = self.controller.get_audiobook_by_author_last_name(C_AUTHOR_LAST_NAME)
            list_with_last_names = list(map(lambda x: x.author_last_name, list_with_a_books))
            self.assertIn(C_AUTHOR_LAST_NAME, list_with_last_names)

        def test_get_audiobook_by_author_first_name(self):
            list_with_a_books = self.controller.get_audiobook_by_author_first_name(C_AUTHOR_FIRST_NAME)
            list_with_first_names = list(map(lambda x: x.author_first_name, list_with_a_books))
            self.assertIn(C_AUTHOR_FIRST_NAME, list_with_first_names)

        def test_get_audiobook_by_category(self):
            list_with_a_books = self.controller.get_audiobook_by_category(C_CATEGORY)
            list_with_categories = list(map(lambda x: x.category, list_with_a_books))
            self.assertIn(C_CATEGORY, list_with_categories)

        def test_get_audiobook_by_release_year(self):
            list_with_a_books = self.controller.get_audiobook_by_release_year(C_RELEASE_YEAR)
            list_with_years = list(map(lambda x: x.release_year, list_with_a_books))
            self.assertIn(C_RELEASE_YEAR, list_with_years)

        def test_get_audiobook__by_publisher(self):
            list_with_a_books = self.controller.get_audiobook_by_publisher(C_PUBLISHER)
            list_with_publishers = list(map(lambda x: x.publisher, list_with_a_books))
            self.assertIn(C_PUBLISHER, list_with_publishers)

        def test_get_audiobook__by_rating(self):
            list_with_a_books = self.controller.get_audiobook_by_rating(8, 10)
            list_with_ratings = list(map(lambda x: x.rating, list_with_a_books))
            self.assertIn(C_RATING, list_with_ratings)

        def test_get_audiobook_by_reader_last_name(self):
            list_with_a_books = self.controller.get_audiobook_by_reader_last_name(C_READER_LAST_NAME)
            list_with_last_names = list(map(lambda x: x.reader_last_name, list_with_a_books))
            self.assertIn(C_READER_LAST_NAME, list_with_last_names)
