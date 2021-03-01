from django.contrib import admin
from guestbook.models import Guestbook

class GuestbookAdmin(admin.ModelAdmin):
    #관리자 화면에서 관리할 필드 목록 정의
    list_display = ("name","email","passwd","content")

admin.site.register(Guestbook, GuestbookAdmin)
