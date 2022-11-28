from django.contrib import admin
from .models import Profile
from elibrary.models import Books

#register our models so the admin can see them in his admin page
admin.site.register(Profile)

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock')  #these are the fields of the books we want to show to the admin page

admin.site.register(Books, BooksAdmin)


