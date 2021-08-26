
from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register,name="register"),
    path('users/',get_userlist,name="users"),
    path('referal/',get_referallist,name="referalall"),
    path('referalspec/<str:pk>',get_spcificCode,name="specific"),
    path('history/',get_history,name="history")
]
