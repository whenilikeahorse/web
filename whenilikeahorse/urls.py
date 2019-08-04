from django.contrib import admin
from django.urls import path, include
import main.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name='main'),
    path('', include('main.urls')),
    path('userQ&A/', include('QandA.urls')),
    path('selfqa/',include('selfqa.urls')),
    path('mypage/',include('mypagemain.urls')),
    path('account/', include('account.urls')),
# =======
# >>>>>>> [Configure rebuild & bootstrap add] 구조 변경 및 부트스트랩 적용
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
