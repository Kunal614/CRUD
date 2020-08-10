from django.contrib import admin

# Register your models here.

from .models import user

@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name'  ,'email','password')
    

