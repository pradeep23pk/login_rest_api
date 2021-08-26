from django.contrib import admin
from api.models import user
from django.contrib import admin
from .models import *

@admin.register(RefCode)
class RefCode(admin.ModelAdmin):
    list_display=['code','from_name','to_name']

@admin.register(history)
class history(admin.ModelAdmin):
    list_display=['usingCode','userEmail','userIncentive','referalEmail','referalIncentive']


@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display=['id','name','email','passwords','referral_code','incentives']
