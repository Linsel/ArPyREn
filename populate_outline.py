import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ArchaeoCod.settings')

import django
django.setup()

## FAKE POPULATION SCRIPT
import random
from outline.models import Person,Publication,Plate,Depiction,Retouch_Depiction,Retouch,Metrics,R_Import,Artefact
from faker import Faker


fake = Faker()
people  = [['Robin','John', 'BA','University of Cologne'],['Andreas','Maier', 'JProf. Dr.','University of Cologne']]

def add_person():
    random_person = random.choice(people)
    t,_ = Person.objects.get_or_create(firstname = random_person [0],surname= random_person[1],title=random_person[2],affiliation=random_person[3])
    #t.save()
    return t

def populate (N=5):
    Faker.seed(0)

    for _ in range (N):
        # get person of entry
        pers = add_person()

        # create fake data for these publication entries

        title = fake.domain_word()
        subtitle = fake.domain_word()
        publisher = fake.street_name()
        place = fake.city()
        doi = fake.mac_address()
        journal = fake.ripe_id()
        issue = fake.port_number()
        ISBN = fake.mac_address()

        # Create new Publications
        publ,_ = Publication.objects.get_or_create(pers_ID = pers, title = title, subtitle = subtitle,publisher = publisher, place = place, doi = doi, journal = journal, issue = issue, ISBN = ISBN)

        page = fake.port_number()
        figure_number = fake.port_number()

        # Create new Plates
        plat,_ = Plate.objects.get_or_create(publ_ID = publ, page = page, figure_number = figure_number, pers_ID = pers)


if __name__ == '__main__':
    print('population script!')
    populate(20)
    print('Population complete!')
