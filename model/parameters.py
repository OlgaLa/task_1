__author__ = 'Властелин Вселенной'
from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name=name
        self.header=header
        self.footer=footer
        self.id=id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class Address:

    def __init__(self, address2, phone2, notes):
        self.address2=address2
        self.phone2=phone2
        self.notes=notes


class Phones:

    def __init__(self, home, mobile, work, fax):
        self.home=home
        self.mobile=mobile
        self.work=work
        self.fax=fax


class Emails:

    def __init__(self, email, email2, email3):
        self.email=email
        self.email2=email2
        self.email3=email3


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, homepage=None, id = None):
        self.middlename=middlename
        self.lastname=lastname
        self.firstname=firstname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.homepage=homepage
        self.id=id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname==other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


