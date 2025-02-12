from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Resim  # Kendi modelini ekle

class StaticViewSitemap(Sitemap):
    """Statik sayfalar için site haritası"""
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about','contact']  # URL isimlerini ekleyin

    def location(self, item):
        return reverse(item)

class ResimSitemap(Sitemap):
    """Model bazlı dinamik URL'ler için site haritası"""
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return Resim.objects.all()  # Model verilerini çeker

