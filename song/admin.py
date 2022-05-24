from django.contrib import admin
from song import models

admin.site.register(models.Artist)
admin.site.register(models.Song)

