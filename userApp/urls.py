from django.urls import path
from userApp.views import user_logout,user_login,user_registration
urlpatterns = [
path('login/',user_login, name="user_login"),
path('logout/',user_logout, name="user_logout"),
path('registration/',user_registration, name="user_registration"),
]
