from django.views.generic.base import RedirectView
from django.urls import path
from .views import * 

app_name="WEB"

urlpatterns = [
    path('',RedirectView.as_view(url='request/'),name="/"),
    path('request/',req,name='req'),
    path('templates/',req),
    path('request/submit',sendreq),
]
