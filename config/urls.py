from django.contrib import admin
from django.urls import path,include
from config import views
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    #관리자용 사이트
    path('admin/', admin.site.urls),

    path('',views.home),
    path('address/', include('address.urls')),
    path('survey/', include('survey.urls')),
    path('guestbook/', include('guestbook.urls')),
    path('member/', include('member.urls')),
    path('youtube/',include('youtube.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/',include(debug_toolbar.urls)),
    ]