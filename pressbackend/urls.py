from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contact.views import ContactViewSet,ReportViewSet
from news.views import NewsViewSet,NoticeViewSet
from committee.views import MemberViewSet,PositionViewSet
from gallery.views import GalleryViewSet
from misc.views import PublicationViewSet

# qr import views
from misc.views import QrView

router = DefaultRouter()
router.register('contacts', ContactViewSet)
router.register('news', NewsViewSet)
router.register('reports', ReportViewSet)
router.register('notices', NoticeViewSet)
router.register('members', MemberViewSet)
router.register('positions', PositionViewSet)
router.register('gallerys',GalleryViewSet)
router.register('misc',PublicationViewSet)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
     path('qr/', QrView.as_view(), name='qr-view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
