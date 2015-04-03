__author__ = 'Властелин Вселенной'
from sys import maxsize
import re


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name=name
        self.header=header
        self.footer=footer
        self.id=id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class Address:

    def __init__(self, address2=None, phone2=None, notes=None):
        self.address2=address2
        self.phone2=phone2
        self.notes=notes


class Phones:

    def __init__(self, homephone=None, mobilephone=None, workphone=None, fax=None):
        self.homephone=homephone
        self.mobilephone=mobilephone
        self.workphone=workphone
        self.fax=fax


class Emails:

    def __init__(self, email=None, email2=None, email3=None):
        self.email=email
        self.email2=email2
        self.email3=email3


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None,
                 title=None, company=None, address=None, homepage=None, homephone=None,
                 mobilephone=None, workphone=None, fax = None, secondaryphone=None, email=None, email2=None, email3=None,
                 address2=None, notes=None,
                 all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.middlename=middlename
        self.lastname=lastname
        self.firstname=firstname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.homepage=homepage
        self.homephone=homephone
        self.mobilephone=mobilephone
        self.workphone=workphone
        self.fax = fax
        self.secondaryphone=secondaryphone
        self.email=email
        self.email2=email2
        self.email3=email3
        self.address2=address2
        self.notes=notes
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page
        self.id=id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname==other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge(self, elements):
        return '\n'.join(filter(lambda x: x != "", map(lambda x: self.clear(x), filter(lambda x: x is not None, elements))))

    def merge_phones(self):
        self.concatenated_phones = self.merge([self.homephone, self.mobilephone, self.workphone, self.secondaryphone])
        return self.concatenated_phones

    def merge_mails(self):
        self.concatenated_mails = self.merge([self.email, self.email2, self.email3])
        return self.concatenated_mails
