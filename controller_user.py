from user import  User

class ControllerUser:
    def __init__(self, session):
        self.session = session

    def add_user(self,fname,lname,email,address,status,wishlist):

        user = User()

        if type(fname)== str and 0< len(fname)< 50:
            user.firstname =fname
        else:
            raise ValueError("this is not a valid first name")

        if type(lname)== str and 0< len(lname)< 50:
            user.lastname =lname
        else:
            raise ValueError("this is not a valid last name")

        if type(email)== str and '@' in email:
            user.email =email
        else:
            raise ValueError("this is not a valid email")

        if type(address)== int:
            user.address =address
        else:
            raise ValueError("this is not a valid last address")

        if status ==1 and status ==2:
            user.status =status
        else:
            raise ValueError("this is not a valid status")

        if type(wishlist) == int:
            user.wishlist =wishlist
        else:
            raise ValueError("this is not a valid wishlist")

        self.session.add(user)
        self.session.commit()
        return user.id

    def change_user(self,id,fname,lname,email,address,status,wishlist):
        try:
            user = self.session.query(User).get(id)
            if user:
                if type(fname)== str and 0< len(fname)< 50:
                    user.firstname =fname
                else:
                    raise ValueError("this is not a valid first name")

                if type(lname)== str and 0< len(lname)< 50:
                    user.lastname =lname
                else:
                    raise ValueError("this is not a valid last name")

                if type(email)== str and '@' in email:
                    user.email =email
                else:
                    raise ValueError("this is not a valid email")

                if type(address)== int:
                    user.address =address
                else:
                    raise ValueError("this is not a valid last address")

                if status ==1 and status ==2:
                    user.status =status
                else:
                    raise ValueError("this is not a valid status")

                if type(wishlist) == int:
                    user.wishlist =wishlist
                else:
                    raise ValueError("this is not a valid wishlist")

                self.session.add(user)
                self.session.commit()
            else:
                raise ValueError("not a valid ID")
        except Exception as e:
            print(e)

    def remove_user(self,id):
        user = self.session.query(User).get(id)
        if user:
            self.session.delete(user)
            self.session.commit
        else:
            raise ValueError("can't find the id you want to delete")
    def get_user(self,id):
        user = self.session.query(User).get(id)
        if user:
            return user
        else:
            raise ValueError("can't find the id you are searching")

    def get_all_user_ids(self):
        users=  self.session.query(User).all()
        ids =[]
        for u in users:
            ids.append(u.id)

    def does_user_excist(self,id):
        if self.session.query(User).all:
            return True
        else: return False

