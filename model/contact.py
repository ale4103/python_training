class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, mobile=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.mobile = mobile
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)

    def __eq__(self, other):
        return  self.id == other.id and self.lastname == other.lastname