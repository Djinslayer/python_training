from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' ' * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", tittle="", company="", address="",
                    home_phone="", mobile_phone="", work_phone="", fax="", mail1="", mail2="", mail3="",
                    homepage="", birthday_year="", anniversary_year="", address2="", phone2="", notes="")] + [
               Contact(firstname=random_string('firstname', 15), middlename=random_string('middlename', 20),
                       lastname=random_string('lastname', 30), nickname=random_string('nickname', 30),
                       tittle=random_string('tittle', 20), company=random_string('company', 30),
                       address=random_string('address', 30), home_phone=random_string('home_phone', 12),
                       mobile_phone=random_string('mobile_phone', 12), work_phone=random_string('work_phone', 12),
                       fax=random_string('fax', 12), mail1=random_string('mail1', 30), mail2=random_string('mail2', 30),
                       mail3=random_string('mail3', 30), homepage=random_string('homepage', 30),
                       bday='9', bmonth='November', birthday_year='1990', aday="20", amonth="April",
                       anniversary_year="2010",
                       address2=random_string('address2', 12), phone2=random_string('phone2', 12),
                       notes=random_string('notes', 12))
               for i in range(5)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))