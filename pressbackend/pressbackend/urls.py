from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contact.views import ContactViewSet,ReportViewSet
from news.views import NewsViewSet,NoticeViewSet
from members.views import MemberViewSet,PositionViewSet


router = DefaultRouter()
router.register('contacts', ContactViewSet)
router.register('news', NewsViewSet)
router.register('reports', ReportViewSet)
router.register('notice', NoticeViewSet)
router.register('commitee', MemberViewSet)
router.register('positions', PositionViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
