from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from audio_book import AudioBook
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
C_READER_LAST_NAME = 'Smith'
C_READER_INCORRECT_LAST_NAME_LONG = str('[i for i in ...]')
C_READER_INCORRECT_LAST_NAME_SHORT = ''
C_READER_FIRST_NAME = 'Black'
C_READER_INCORRECT_FIRST_NAME_LONG = str('[i for i in ...]')
C_READER_INCORRECT_FIRST_NAME_SHORT = ''
C_READER_MIDDLE_NAME = 'Nil'
C_READER_INCORRECT_MIDDLE_NAME_LONG = str('[i for i in ...]')
C_READER_INCORRECT_MIDDLE_NAME_SHORT = ''
C_DURATION_HOURS = 2
C_DURATION_MINUTES = 50
C_DURATION_SECONDS = 34


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
        self.assertEqual(ab_from_query.book_title, audio_book.book_title)
        self.assertEqual(ab_from_query.author_last_name, audio_book.author_last_name)
        self.assertEqual(ab_from_query.author_first_name, audio_book.author_first_name)
        self.assertEqual(ab_from_query.author_middle_name, audio_book.author_middle_name)
        self.assertEqual(ab_from_query.release_year, audio_book.release_year)
        self.assertEqual(ab_from_query.rating, audio_book.rating)
        self.assertEqual(ab_from_query.pic, audio_book.pic)
        self.assertEqual(ab_from_query.category, audio_book.category)
        self.assertEqual(ab_from_query.language, audio_book.language)
        self.assertEqual(ab_from_query.annotation, audio_book.annotation)
        self.assertEqual(ab_from_query.publisher, audio_book.publisher)
        self.assertEqual(ab_from_query.reader_first_name, audio_book.reader_first_name)
        self.assertEqual(ab_from_query.reader_middle_name, audio_book.reader_middle_name)
        self.assertEqual(ab_from_query.reader_last_name, audio_book.reader_last_name)
        self.assertEqual(ab_from_query.duration_hours, audio_book.duration_hours)
        self.assertEqual(ab_from_query.duration_minutes, audio_book.duration_minutes)
        self.assertEqual(ab_from_query.duration_seconds, audio_book.duration_seconds)

