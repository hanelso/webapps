"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import helloweb.views as helloweb_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloweb/hello', helloweb_views.hello),
    # path 는 urls.py에게 참조할 위치를 알려주는 것이기 때문에 위치와 이름만 알려주면 된다.(mapping)
    # -> 그래서 views에 있는 hello 메소드를 호출 하는것이 아닌 hello라는 메소드 이름으로 mapping하는 것이다.
    path('helloweb/tags', helloweb_views.tags),
    # HTML tag들의 연습을 위해서 만든 메소드.
]
