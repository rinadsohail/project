from django.contrib import admin
from .models import Post

# renders the post onto the homescreen 
admin.site.register(Post)
