from django.contrib import admin

from .models import Question,Choice,Questiongramm,Choicegramm

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Questiongramm)
admin.site.register(Choicegramm)
