from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# center of investigation, the physical artefact
class UserProfileInfo (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional attributes
    affiliation = models.CharField(max_length=200,blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username


class Artefact(models.Model):
    arte = models.CharField(max_length=200)
    arte_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,blank=True)
    rawmaterial = models.CharField(max_length=200,blank=True)
    type = models.CharField(max_length=200,blank=True)
    classification = models.CharField(max_length=200,blank=True)


# actor, publisher, drawer, multiple functions
class Person(models.Model):
    firstname = models.CharField(max_length=200,blank=True)
    surname = models.CharField(max_length=200,blank=True)
    title = models.CharField(max_length=200,blank=True)
    affiliation = models.CharField(max_length=200,blank=True)
    #email = models.EmailField(max_length=200,blank=True)

    def __str__(self):
        return self.firstname + ' ' + self.surname

#
class Publication(models.Model):
    people = models.ManyToManyField(Person)
    title = models.CharField(max_length=200,blank=True)
    subtitle = models.CharField(max_length=200,blank=True)
    publisher = models.CharField(max_length=200,blank=True)
    place = models.CharField(max_length=200,blank=True)
    doi = models.CharField(max_length=200,blank=True)
    journal = models.CharField(max_length=200,blank=True)
    issue = models.CharField(max_length=200,blank=True)
    ISBN = models.CharField(max_length=200,blank=True)

#
class Plate(models.Model):
    publications = models.ManyToManyField(Publication)
    person = models.ForeignKey(Person, on_delete=models.CASCADE,blank=True) # creator
    figurenumber = models.IntegerField(blank=True)
    page = models.IntegerField(blank=True)
    depictiontype = models.CharField(max_length=200,blank=True)
    plat_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,blank=True)


#
class Depiction(models.Model):
    plates = models.ManyToManyField(Plate)
    arte = models.ForeignKey(Artefact, on_delete=models.CASCADE,blank=True)#
    depiction_name = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField('date published',blank=True)
    outline = models.CharField(max_length=200,blank=True)
    depi_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,blank=True)


class Retouch_Depiction(models.Model):
    depi = models.ForeignKey(Depiction, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE,blank=True)#) # Editor
    version = models.CharField(max_length=200,blank=True)
    rede_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,blank=True)

class Retouch (models.Model):
    rede = models.ForeignKey(Retouch_Depiction, on_delete=models.CASCADE)
    retouch_name = models.CharField(blank=True,max_length=200)
    length = models.FloatField(blank=True,max_length=200)
    location = models.CharField(blank=True,max_length=200)

#
class Metrics(models.Model):
    depi = models.ForeignKey(Depiction, on_delete=models.CASCADE)
    width = models.FloatField(blank=True)
    length = models.FloatField(blank=True)
    l_w_index = models.FloatField(blank=True)
    area = models.FloatField(blank=True)
    percent_area = models.FloatField(blank=True)
    contour_length = models.FloatField(blank=True)
    length_lower_part = models.FloatField(blank=True)
    length_upper_part = models.FloatField(blank=True)
    width_left_part = models.FloatField(blank=True)
    width_right_part = models.FloatField(blank=True)
    tip_angle = models.FloatField(blank=True)
    MP_CM_x_offset = models.FloatField(blank=True)
    MP_CM_y_offset = models.FloatField(blank=True)


#
class R_Import(models.Model):
    depi = models.ForeignKey(Depiction, on_delete=models.CASCADE)
    cluster = models.IntegerField(blank=True)
