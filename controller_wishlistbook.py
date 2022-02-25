from wishlistbook import WishlistBook
from database import session
from controller_wishlist import ControllerWishlist
from controller_book import ControllerBook


class ControllerWishlistBook:

    @staticmethod
    def add_book_to_wishlist(id_wishlist, id_book):
        wishlist_book = WishlistBook()
        if id_wishlist in ControllerWishlist.get_all_ids():
            wishlist_book.id_wishlist = id_wishlist
            if id_book in ControllerBook.get_all_ids():
                wishlist_book.id_book = id_book
            else:
                raise ValueError('Book with this ID does not exist in data base')
        else:
            raise ValueError('Wishlist with this ID does not exist in data base')

    @staticmethod
    def delete_book_from_wishlist(id_wishlist_to_book):
        try:
            book_to_wishlist = session.query(WishlistBook).get(id_wishlist_to_book)
            if book_to_wishlist:
                session.delete(book_to_wishlist)
                session.commit()
            else:
                raise ValueError(f'Relation with this ID {id_wishlist_to_book} does not exist in data base')
        except Exception as e:
            print(e)

    @staticmethod
    def get_all_ids_books_by_wishlist(id_wishlist):
        if id_wishlist in ControllerWishlist.get_all_ids():
            id_books = session.query(WishlistBook).filter(WishlistBook.id_wishlist == id_wishlist).all()
            return id_books
        else:
            raise ValueError('Wishlist with this ID does not exist in data base')
