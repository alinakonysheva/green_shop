def do_run():
    from database import create_database, engine, session
    create_database(engine, do_erase=True)

    """eb = EBook()
    eb.size = 25
    eb.book_title = 'Ebook_1'
    eb.author_first_name = 'author'
    eb.language = 'af'
    eb.category = 2
    eb.publisher = 'alpina'
    eb.release_year = 2000
    eb.rating = 5
    eb.annotation = 'annotation to the Ebook_1 of author'
    eb.author_last_name = 'lastnameauthor'
    eb.author_middle_name = 'middlenameauthor'
    session.add(eb)
    session.commit()"""


if __name__ == '__main__':
    do_run()
