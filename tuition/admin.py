from django.contrib import admin

from tuition.models import Level, Subject, Tuition, Rating



# Register your models here.
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Tuition)
admin.site.register(Rating)