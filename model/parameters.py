__author__ = 'Властелин Вселенной'


class Group:

    def __init__(self, name=None, header=None, footer=None):
        self.name=name
        self.header=header
        self.footer=footer


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

    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, homepage):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.homepage=homepage



