from django.urls import path
from guestbook import views

urlpatterns = [
    #방명록 관련 url
    path('', views.list),
    path('write', views.write),
    path('gb_insert', views.insert),
    path('passwd_check', views.passwd_check),
    path('gb_update', views.update),
    path('gb_delete', views.delete),
]