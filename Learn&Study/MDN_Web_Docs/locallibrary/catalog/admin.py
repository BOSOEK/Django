from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance
# 모델 등록 : admin.site.register(모델)
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin) :
    list_distplay = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# 관련 모델에 관리자 클래스 등록
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin) :
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin) :
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields' : ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields' : ('status', 'due_back')
        }),
    )
