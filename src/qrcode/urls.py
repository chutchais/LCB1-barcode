"""qrcode URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500
from django.conf.urls import include, url
# from . import views
from .views import qr_image,read_qr,billing_qr_image,billing_barcode_image,barcode_image

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^read/', read_qr,name='read'),
    url(r'^(?P<data>[-\w]+)/$', qr_image, name='create'),
    url(r'^barcode/(?P<data>[-\w]+)/$', barcode_image, name='bar'),
	url(r'^billing/qr', billing_qr_image, name='qr'),
    url(r'^billing/barcode', billing_barcode_image, name='barcode'),
    # url(r'^text/', include(('text.urls','text')), name='barcode'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# .+
# url(r'(?P<data>[\w\-]+)/$', qr_image, name='create'),
# url(r'(?P<data>.+/$', qr_image, name='create'),