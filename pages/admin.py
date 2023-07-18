from django.contrib import admin
from .models import Page ,Books
# Register your models here.
class PageAdmin(admin.ModelAdmin):
	list_display=('title', 'update_date')
	ordering=('title',)
	search_fields=('title',)

class BooksAdmin(admin.ModelAdmin):
	list_display=('title', 'linktoamazon')
	ordering=('title',)





admin.site.register(Page, PageAdmin)
admin.site.register(Books,BooksAdmin)