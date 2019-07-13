from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserqaList.as_view(), name="userqalist"),
    path('new_qa/', views.new_qa, name = "new_qa" ),
    path('qa_detail/<int:pk>', views.Qa_detail.as_view(), name = "userqa_detail" ),
]