from django.contrib import admin
from .models import Post,AuthorRegister

# Register your models here.
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ["id","title","description"]

@admin.register(AuthorRegister)
class Authoradmin(admin.ModelAdmin):
    list_display = ["id","firstname","username","age"]