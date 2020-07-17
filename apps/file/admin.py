from django.contrib import admin

# Register your models here.
from apps.file.models import File

admin.site.register(File)