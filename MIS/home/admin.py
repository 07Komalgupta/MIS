from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(LoginUser)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Module)
admin.site.register(Student)