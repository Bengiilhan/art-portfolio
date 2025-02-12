from django.contrib import admin
from .models import Resim

class ResimAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')  # Admin panelinde hangi alanların görüneceği
    search_fields = ('title', 'description')  # Arama yapılacak alan
    list_filter = ('title',)  # Filtreleme alanı

admin.site.register(Resim, ResimAdmin)

# Register your models here.
