from django.urls import path, re_path
from django.contrib import admin
from images.views import BarcodeDataView
from admins.views import ImagesManageView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('api/_manage/admin/', admin.site.urls),
    path('api/_manage/images/', ImagesManageView.as_view(), name='manage_images'),
    # path('api/_manage/images/<int:pk>', ImagesManageView.as_view(), name='delete_image'),
    path('api/save-barcode/', BarcodeDataView.as_view(), name='save_barcode_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]