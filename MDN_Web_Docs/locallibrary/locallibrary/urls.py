# 사이트의 URL과 뷰의 연결을 지정, 여기에는 모든 URL 매핑 코드가 포함 될 수 있지만, 특정 어플리케이션에 매핑의 일부를 할당해주는 것이 일반적

"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
예제:
Function views 일 경우
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views 일 경우
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
다른 참조할 URL FILE들을 포함시켜야 하는 경우
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# catalog 애플리케이션에서 경로를 추가하려고 include() 사용
from django.urls import include
# URL 맵을 추가해 기본 URL을 애플리케이션으로 리디렉션
from django.views.generic import RedirectView
# static()으로 url매핑을 추가하여 개발 중 정적 파일을 제공함
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# www.xxxx.com/catalog 로 요청이 들어오면 catalog/urls.py를 참조해 맵핑한다는 뜻
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# 사이트 URL을 localhost:8000에서 localhost:8000/catalog/로 리다이렉트 함
urlpatterns += [
    # 첫번째 매개변수를 비워놓으면 '/'을 의미한다
    # 만약 매개변수를 '/'라고 작성시 오류가 발생한다
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# 개발중 정적 파일들(css, js)을 제공하는 것 허용
urlpatterns == static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
