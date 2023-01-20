from django.urls import path, include
from . import views
app_name='cartapp'

urlpatterns = [
path('',views.allProductCat,name='allProductCat'),
path('<slug:c_slug>/',views.allProductCat,name='products_by_category'),
path('<slug:c_slug>/<slug:p_slug>/',views.proDetail,name='pc_details')
]