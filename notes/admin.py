from django.contrib import admin
from notes import models

admin.site.register(models.Note)
admin.site.register(models.Tag)
