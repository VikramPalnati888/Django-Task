from django.urls import path
from Bopbo_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('test/', sheet,name='test'),
	
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
