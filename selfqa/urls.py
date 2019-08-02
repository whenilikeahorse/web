from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name="selfqa"),
    path('', views.QaView.as_view(), name='selfqa'),
    path('newqa/', views.QaCreate.as_view(), name='new'),
    path('detail/<int:pk>', views.QaDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.QaUpdate.as_view(), name='change'),
    path('delete/<int:pk>', views.QaDelete.as_view(), name='del'),

]