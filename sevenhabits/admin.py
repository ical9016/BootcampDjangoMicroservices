from django.contrib import admin

# Register your models here.
from sevenhabits.models import Roles, Goals

admin.site.register(Roles)
admin.site.register(Goals)
