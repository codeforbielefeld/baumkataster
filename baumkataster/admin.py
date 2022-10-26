from django.contrib import admin

# Register your models here

from .models import Tree
from .models import User

admin.site.register(Tree)
admin.site.register(User)
