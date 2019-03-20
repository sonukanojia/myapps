from django.contrib import admin
from .models import Employee

# Register your models here.


class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ('eid' , 'ename' , 'econtact')


admin.site.register(Employee,UserRegisterAdmin)