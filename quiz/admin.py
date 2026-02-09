from django.contrib import admin
from .models import TechDomain, Question, Choice, Resource

# This tells the Admin panel to show these tables
admin.site.register(TechDomain)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Resource)