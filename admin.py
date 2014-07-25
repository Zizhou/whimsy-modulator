from django.contrib import admin
from whimsy.models import Sentence

# Register your models here.

class SentenceAdmin(admin.ModelAdmin):
    fields = ['sentence', 'submitter']

admin.site.register(Sentence)
