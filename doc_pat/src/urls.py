from django.conf.urls import url
from .views import *
from django.urls import path

urlpatterns = [
    path('', index),
    url(r'^pdf/(?P<user_id>[0-9]+)/$', GeneratePdf.as_view(), name='generatepdf')
]
