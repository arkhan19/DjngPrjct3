from django.contrib import admin
from vs.posts import models
# Register your models here.
admin.site.register(models.Posts)  # to show Post table in admin page
