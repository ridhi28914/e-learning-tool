from django.contrib import admin

from .models import Question,Choice,Questionmaths,Choicemaths

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Questionmaths)
admin.site.register(Choicemaths)
