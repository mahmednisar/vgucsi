from django.contrib import admin

# Register your models here.
from .models import Blogpost, Contact, Team, Event, Homebanner

admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Blogpost)
admin.site.register(Event)
admin.site.register(Homebanner)