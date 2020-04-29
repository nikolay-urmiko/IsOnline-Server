from django.contrib import admin
from .models import Checks, Ur_face


class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(Checks)
    admin.site.register(Ur_face)
    

