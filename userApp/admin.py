from django.contrib import admin
from userApp.models import UserProfile

# Register your models here.


class userProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'city','phone']
    list_filter = ['user']


admin.site.register(UserProfile,userProfileAdmin)
