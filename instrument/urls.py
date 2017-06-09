from django.conf.urls import url
from . import views

urlpatterns = [
    url("^", views.instrument_list, name='instrument-list')
]