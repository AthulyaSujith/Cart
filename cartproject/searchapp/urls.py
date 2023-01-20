from django.urls import path, include
from . import views
app_name='searchapp'

urlpatterns=[
path('search/',views.searchResult,name='searchResult')
]