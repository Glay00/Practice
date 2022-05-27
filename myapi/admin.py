
# Register your models here.
from django.contrib import admin
from .models import Title, TextField

# class TitleAdmin(admin.ModelAdmin):
#     model = Title

# admin.site.register(Title, TitleAdmin)
admin.site.register(Title)
