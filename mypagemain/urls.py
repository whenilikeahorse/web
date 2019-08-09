from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="mypagemain"),
    path('timeline/', views.PfView.as_view(), name="timeline"),
    path('portfolio/new', views.PfCreate.as_view(), name='new_pf'),
    path('portfolio/detail/<int:pk>', views.PfDetail.as_view(), name='detail_pf'),
    path('portfolio/update/<int:pk>', views.PfUpdate.as_view(), name='change_pf'),
    path('portfolio/delete/<int:pk>', views.PfDelete.as_view(), name='del_pf'),
]