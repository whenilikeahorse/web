from django.contrib import admin
from django.urls import path, include
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name='main'),
    path('', include('main.urls')),
    path('userQ&A/', include('QandA.urls')),
    path('selfqa/',include('selfqa.urls')),
    path('mypage/',include('mypagemain.urls')),
    path('account/', include('account.urls')),
]
