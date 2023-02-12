
from django.contrib import admin
from .models import Agent, Management, Other


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'team', 'favourite_food']


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'designation', 'favourite_food']


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'department']


