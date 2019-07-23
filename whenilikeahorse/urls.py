from django.contrib import admin
from django.urls import path, include
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name='main'),
    path('', include('main.urls')),
    path('userQ&A/', include('QandA.urls')),
# <<<<<<< HEAD
    path('mypage/',include('mypagemain.urls')),
    path('account/', include('account.urls')),
# =======
# >>>>>>> [Configure rebuild & bootstrap add] 구조 변경 및 부트스트랩 적용
]
