from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'index' ),
    path('other_page/<int:user_id>', views.other_page, name="other_page"),
    path('search_page/', views.search_page, name="search_page"),
    path('search/', views.search, name="search"),
]