from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name="apiOverview"),
    path('', views.productalllist, name="productalllist"),
]
