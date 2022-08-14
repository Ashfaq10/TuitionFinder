from django.contrib import admin

from tuition.models import Level, Subject, Tuition



# Register your models here.
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Tuition)