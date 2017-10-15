import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Fake population script.
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

# Topics
fakegen = Faker()
topics = [
    'Search',
    'Social',
    'Marketplace',
    'News',
    'Games',
]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

#
def populate(N=5):
    for entry in range(N):
        # Get the topic for the entry.
        top = add_topic()

        # Create the fake data for the entry.
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new Webpage entry.
        webpage = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        # Create a fake access record for the new Webpage.
        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script...")
    populate(20)
    print("Populating Complete.")
