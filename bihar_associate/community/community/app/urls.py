
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
import app.views as appView
from django.views.generic.base import RedirectView


urlpatterns = [

    url(r'^$', appView.gallery, name='gallery'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    url(r'^(?P<slug>[-\w]+)$', appView.AlbumDetail.as_view(), name='album'),
    # app.views.AlbumView.as_view()

    # Auth related urls

    url(r'^accounts/login/$', views.LoginView, name='login'),
    url(r'^logout$', views.LogoutView, {'next_page': '/', }, name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)