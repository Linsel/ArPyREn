from django.contrib import admin
from outline.models import Person,Publication,Plate,Depiction,Retouch_Depiction,Retouch,Metrics,R_Import,Artefact,UserProfileInfo

# Register your models here.

admin.site.register(Person)
admin.site.register(Publication)
admin.site.register(Plate)
admin.site.register(Depiction)
admin.site.register(Retouch_Depiction)
admin.site.register(Retouch)
admin.site.register(Metrics)
admin.site.register(R_Import)
admin.site.register(Artefact)
admin.site.register(UserProfileInfo)
