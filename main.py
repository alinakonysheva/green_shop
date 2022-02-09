
# Een “webshop” maken. In onze webshop verkopen we boeken, zowel fysieke als audio als voor een e reader.
# Elk boek heeft uiteraard een paar eigenschappen. Elke klant heeft uiteraard ook een paar eigenschappen
# Wat moet er gemaakt worden:
# - een klantenbestand
#  - product pagina(’s)
#  - gemakkelijke filters op product
#  - login/wachtwoord reset
#  - een wenslijst van een klant, een klant kan dus een boek op zijn wenslijst zetten en uiteraard daar
# ook afhalen
# Note: het is niet de bedoeling dat we een betaal en/of facturatie systeem en dergelijke gaan toevoegen.
# Ook geen shopping cart

def do_run():
    from database import create_database, engine, session
    create_database(engine)
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
