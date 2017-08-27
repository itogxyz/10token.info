from django.contrib import admin
from .models import Startup

class StartupAdmin(admin.ModelAdmin):
    list_display = ('name','amount','token_id','created_date')
    list_filter = ('reissuable',)
    search_fields = ('name','amount','token_id','created_date')

admin.site.register(Startup, StartupAdmin)
