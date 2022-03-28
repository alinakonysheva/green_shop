from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, RadioField, TextAreaField


class EbookForm(FlaskForm):
    title = StringField('EBook title', id='ebook_title')
    author_first_name = StringField('Author first name', id='ebook_author_first_name')
    author_last_name = StringField('Author last name', id='ebook_author_last_name')
    # TODO: this field is allowed to be empty, redo
    author_middle_name = StringField('Author middle name', id='ebook_author_middle_name')
    release_year = IntegerField('Release year', id='ebook_release_year')
    rating = FloatField('Rating', id='ebook_rating')
    # TODO:
    pic = StringField('Link to the picture', id='ebook_pic')
    category = IntegerField('Category', id='ebook_category')
    language = RadioField('Language', choices=[('ru', 'Russian'), ('nl', 'Nederlands'), ('en', 'English')],
                          id='ebook_language')
    annotation = TextAreaField('Annotation', id='ebook_annotation')
    publisher = StringField('Publisher', id='ebook_publisher')
    size = FloatField('Size in Mb', id='ebook_size')

    submit = SubmitField('Save', id='ebook_submit')


class AudiobookForm(FlaskForm):
    title = StringField('Audiobook title', id='audiobook_title')
    author_first_name = StringField('Author first name', id='audiobook_author_first_name')
    author_last_name = StringField('Author last name', id='audiobook_author_last_name')
    # TODO: this field is allowed to be empty, redo
    author_middle_name = StringField('Author middle name', id='audiobook_author_middle_name')
    release_year = IntegerField('Release year', id='audiobook_release_year')
    rating = FloatField('Rating', id='audiobook_rating')
    # TODO:
    pic = StringField('Link to the picture', id='audiobook_pic')
    category = IntegerField('Category, number', id='audiobook_category')
    language = RadioField('Language', choices=[('ru', 'Russian'), ('nl', 'Nederlands'), ('en', 'English')],
                          id='audiobook_language')
    annotation = TextAreaField('Annotation', id='audiobook_annotation')
    publisher = StringField('Publisher', id='audiobook_publisher')
    reader_first_name = StringField('Reader, first name', id='audiobook_reader_first_name')
    reader_last_name = StringField('Reader, last name', id='audiobook_reader_last_name')
    reader_middle_name = StringField('Reader, middle name', id='audiobook_reader_middle_name')
    duration_hours = IntegerField('Duration, hours', id='audiobook_duration_hours')
    duration_minutes = IntegerField('Duration, minutes', id='audiobook_duration_minutes')
    duration_seconds = IntegerField('Duration, seconds', id='audiobook_duration_seconds')

    submit = SubmitField('Save', id='audiobook_submit')


class PaperbookForm(FlaskForm):
    title = StringField('Paper book title', id='paperbook_title')
    author_first_name = StringField('Author first name', id='paperbook_author_first_name')
    author_last_name = StringField('Author last name', id='paperbook_author_last_name')
    # TODO: this field is allowed to be empty, redo
    author_middle_name = StringField('Author middle name', id='paperbook_author_middle_name')
    release_year = IntegerField('Release year', id='paperbook_release_year')
    rating = FloatField('Rating', id='paperbook_rating')
    # TODO:
    pic = StringField('Link to the picture', id='paperbook_pic')
    category = IntegerField('Category, number', id='paperbook_category')
    language = RadioField('Language', choices=[('ru', 'Russian'), ('nl', 'Nederlands'), ('en', 'English')],
                          id='paperbook_language')
    annotation = TextAreaField('Annotation', id='paperbook_annotation')
    publisher = StringField('Publisher', id='paperbook_publisher')

    cover = RadioField('Cover', choices=[(1, 'Soft'), (2, 'Hard')], id='paperbook_cover')
    length = IntegerField('Length in cm', id='paperbook_length')
    width = IntegerField('Width in cm', id='paperbook_width')
    weight = IntegerField('Weight in gr', id='paperbook_weight')
    pages = IntegerField('Number of pages', id='paperbook_pages')
    isbn = StringField('ISBN, 13 digits', id='paperbook_isbn')
    submit = SubmitField('Save', id='paperbook_submit')

