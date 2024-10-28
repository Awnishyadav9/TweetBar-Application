from django.contrib import admin
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ('text','photo','created_at','update_at')
    
admin.site.register(Tweet,TweetAdmin)
