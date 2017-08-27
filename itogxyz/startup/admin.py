from django.contrib import admin
from .models import *

class StartupAdmin(admin.ModelAdmin):
    list_display = ('name','user','goal','created_date')
    list_filter = ('created_date',)
    search_fields = ('name','description','wallet')

class InvestorAdmin(admin.ModelAdmin):
    list_display = ('user','created_date')
    # list_filter = ('reissuable',)
    search_fields = ('user',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('investor','startup','amount')
    list_filter = ('amount','startup')
    search_fields = ('investor','startup')

admin.site.register(Startup, StartupAdmin)
admin.site.register(Investor, InvestorAdmin)
admin.site.register(Order, OrderAdmin)
