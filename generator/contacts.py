from model.parameters import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o=="-n":
        n=int(a)
    elif o=="-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation  +" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company='',
                      address='', homephone='', mobilephone='', workphone='', email2='', email='', email3='',
                      homepage='', address2='', secondaryphone='', notes='')] + [Contact(lastname=random_string("ln", 10), firstname=random_string("fn", 10),
             middlename=random_string("mn", 10), nickname=random_string("nn", 3),
             title=random_string("t", 10), company=random_string("co", 10), address=random_string("add", 10),
             mobilephone=random_string("mp", 10), homephone=random_string("hp", 10),
             workphone=random_string("wp", 10), email2=random_string("e2", 10),
             email=random_string("e", 10), email3=random_string("e3", 10), homepage=random_string("hp", 10),
             address2=random_string("add2", 20), secondaryphone=random_string("sph", 10), notes=random_string("notes", 10))
     for i in range (n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)


with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))