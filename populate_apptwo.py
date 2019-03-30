import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## fake population script
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()
# topics = ['Search','Social','Marketplace','News','Games']

# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t


def populate(N=5):
    for entry in range(N):

        #create fake data
        fake_firstName = fakegen.first_name()
        fake_lastName = fakegen.last_name()
        fake_email= fakegen.email()

        # Create the new webpage entry
        user = User.objects.get_or_create(FirstName=fake_firstName,LastName=fake_lastName,Email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")