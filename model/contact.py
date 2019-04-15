from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, homephone=None, workphone=None,
                 mobile=None, secondaryphone=None, id=None, all_phones_from_home_page=None,
                 email=None, email2=None, email3=None, all_emails=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobile = mobile
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails = all_emails
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.lastname == other.lastname and self.firstname == other.firstname or self.all_phones_from_home_page == other.all_phones_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize