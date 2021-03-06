from address import Address
from user import  User


class ControllerAddress:
    def __init__(self, session):
        self.session = session

    def add_address(self, street, number, postcode, city, country):
        address = Address()

        if type(street) == str and 0 < len(street) < 88:
            address.street = street
        else:
            raise ValueError("not a valid street name")

        if type(number) == str and 0 < len(number) <= 10:
            address.number = number
        else:
            raise ValueError("not a valid street number")

        if type(postcode) == str and 0 < len(number) <= 30:
            address.postcode = postcode
        else:
            raise ValueError("not a valid postcode")

        if type(city) == str and 0 < len(city) < 88:
            address.city = city
        else:
            raise ValueError("not a valid city name")

        if type(country) == str and 0 < len(street) < 56:
            address.country = country
        else:
            raise ValueError("not a valid country name")

        self.session.add(address)
        self.session.commit()
        return address.id

    def change_address(self, id, street, number, postcode, city, country):
        try:
            address = self.session.query(Address).get(id)
            if address:
                if type(street) == str and 0 < len(street) < 88:
                    address.street = street
                else:
                    raise ValueError("not a valid street name")

                if type(number) == str and 0 < len(number) < 10:
                    numbers = "0123456789"
                    n= numbers.split()
                    for v in n:
                        if v in numbers:
                            address.number = number
                else:
                    raise ValueError("not a valid street number")

                if type(postcode) == str:
                    address.postcode = postcode
                else:
                    raise ValueError("not a valid street number")

                if type(city) == str and 0 < len(city) < 88:
                    address.city = city
                else:
                    raise ValueError("not a valid city name")

                if type(country) == str and 0 < len(street) < 56:
                    address.country = country
                else:
                    raise ValueError("not a valid country name")
            else:
                raise ValueError("not a valid id")
        except Exception as e:
            print(e)

    def remove_address(self, id):
        address = self.session.query(Address).get(id)
        if address:
            self.session.delete(address)
            self.session.commit()
        else:
            raise ValueError("can't find the id that you want to delete")

    def get_address(self, id):
        address = self.session.query(Address).get(id)
        if address:
            return address
        else:
            raise ValueError("can't find the id you are searching")

    def get_address_by_street(self, search):
        address_list = self.session.query(Address).filter(Address._street.like(search)).all()
        return address_list

    def get_address_by_number(self, search):
        address_list = self.session.query(Address).filter(Address._number.like(search)).all()
        return address_list

    def get_address_by_city(self, search):
        address_list = self.session.query(Address).filter(Address._city.like(search)).all()
        return address_list

    def get_address_by_postcode(self, search):
        address_list = self.session.query(Address).filter(Address._postcode.like(search)).all()
        return address_list

    def get_address_by_country(self, search):
        address_list = self.session.query(Address).filter(Address._country.like(search)).all()
        return address_list

    def get_address_by_user_firstname(self,search):
        users = self.session.query(User).filter(User._firstname.like(search)).all()
        address_list = []
        for user in users:
            address_list.append(user.address)
        return address_list



    def get_address_by_user_lastname(self,search):
        address_list = self.session.query(Address).join(User).filter(User._lastname.like(search)).all()
        return address_list
