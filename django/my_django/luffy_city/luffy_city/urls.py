"""luffy_city URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from Polyv import views as Polyvviews
from login import views as Loginviews
from login import geetest_views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/course/', include("Course.urls")),
    url(r'^api/polyv/', Polyvviews.PolyvView.as_view()), #保利威视频

# 购物分发
    url(r'^api/shopping/', include("shopping.urls")), #购物车
#     url(r'^api/polyv', PolyvView.as_view()),
    # 登录注册
    url(r'^register/', Loginviews.RegisterView.as_view()), #注册
    # # geetest demo
    url(r'^$', views.demo),
    # url(r'^pc-geetest/register', views.pcgetcaptcha, name='pcgetcaptcha'),
    url(r'^pc-geetest/register', Loginviews.GeetestView.as_view(), name='pcgetcaptcha'), #滑动验证码登录
    # url(r'^mobile-geetest/register/', views.mobilegetcaptcha, name='mobilegetcaptcha'),
    url(r'^pc-geetest/validate/', views.pcvalidate, name='pcvalidate'),
    # url(r'^pc-geetest/ajax_validate',views.pcajax_validate, name='pcajax_validate'),
    url(r'^pc-geetest/ajax_validate',Loginviews.GeetestView.as_view(), name='pcajax_validate'),#滑动验证码登录二次验证
    # url(r'^mobile-geetest/ajax_validate/',views.mobileajax_validate, name='mobileajax_validate'),

    # media路径配置
    url(r'media/(?P<path>.*)/$', serve, {'document_root': settings.MEDIA_ROOT})
    # img  src= "http://127.0.0.1:81；00/media/teacher/2018-12/wenzhou.jpg"
]
