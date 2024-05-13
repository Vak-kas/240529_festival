from django.contrib import admin
from .models import User, BackUp


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ['nickname', 'name', 'hobby', 'gender', 'age']

class BackupAdmin(admin.ModelAdmin):
    search_fields = ['nickname', 'name', 'hobby', 'gender', 'age']



admin.site.register(User, UserAdmin)
admin.site.register(BackUp, BackupAdmin)


