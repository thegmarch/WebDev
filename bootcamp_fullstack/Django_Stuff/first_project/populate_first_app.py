import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

## Fake Pop Script
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    """
    Create N entries of Dates Accessed
    """

    for entry in range(N):
        #Get topic for entry
        top = add_topic()

        #create fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()

        #create new Webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create fake Access Record for that Page
        #can add more entrys by not neccessary
        accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Pupulating database.. Please Wait")
    populate(20)
    print("Populate complete")
