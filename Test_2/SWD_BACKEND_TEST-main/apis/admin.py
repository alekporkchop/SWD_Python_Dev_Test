from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(SchoolStructure)
admin.site.register(Schools)
admin.site.register(Classes)
admin.site.register(Personnel)
admin.site.register(Subjects)
admin.site.register(StudentSubjectsScore)