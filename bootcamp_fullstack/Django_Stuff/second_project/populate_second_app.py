import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()

import random
from project_two_app.models import Users
from faker import Faker

fakegen = Faker()


def make_person(N=5):
    for entry in range(N):

        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        usr = Users.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,usr_email=fake_email)[0]

if __name__ == '__main__':
    print("populating script")
    make_person(20)
    print("done populating")
