from django.contrib import admin

# Register your models here.
from .models import professor
from .models import reviews

admin.site.register(professor)
admin.site.register(reviews)