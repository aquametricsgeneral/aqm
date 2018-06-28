from django.contrib import admin
from .models import Post

class MyAdmin(admin.ModelAdmin):
  date_hierarchy = 'published_date'
  search_fields = ['published_date','title','text']
  list_display = ('published_date','title','text','value')
  list_filter = ('published_date',)

admin.site.register(Post, MyAdmin)