from django.contrib import admin
from .models import AdminProfile, Jadval, Author, Books

# Register your models here.

admin.site.register(AdminProfile)
admin.site.register(Jadval)
admin.site.register(Author)
admin.site.register(Books)
