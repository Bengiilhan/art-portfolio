from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from resume.sitemaps import StaticViewSitemap, YourModelSitemap

sitemaps = {
    'static': StaticViewSitemap(),
    'models': YourModelSitemap(),
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', views.home,name='home'),
    path("about/",views.about,name="about"),
    path("painting/", views.painting, name="painting"),
    path("contact/", views.contact, name="contact")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)