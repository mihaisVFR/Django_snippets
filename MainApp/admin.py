from django.contrib import admin
from django.contrib import admin
from MainApp.models import Snippet, Comment, Langs

admin.site.register(Snippet)
admin.site.register(Comment)
admin.site.register(Langs)

# Register your models here.
